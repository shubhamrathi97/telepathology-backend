from backend.models import BaseModel, models
from Address.models import Address, AddressSerializer
from Images.models import ImageBatch, ImageBatchSerializer
from Doctor.models import Doctor, DoctorSerializer
from Operator.models import Operator, OperatorSerializer
from User.models import User, UserSerializer
from rest_framework import serializers


class Patient(BaseModel):
    name = models.TextField(null=True)
    mobile = models.TextField(null=False)
    age = models.TextField(null=True)
    gender = models.TextField(null=True)
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
            models.Index(fields=['mobile'], name='mobile_idx'),
        ]


class PatientSerializer(serializers.ModelSerializer):
    address = AddressSerializer(allow_null=True, required=False)

    class Meta:
        model = Patient
        fields = '__all__'


class Sample(BaseModel):
    sample_type = models.TextField(null=False)
    # note = JSONField(null=True, default=list)
    batch = models.ForeignKey(ImageBatch, on_delete=models.SET_NULL, related_name='batch_sample', null=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, related_name='patient_sample', blank=True, null=True)
    operator_id = models.ForeignKey(Operator, on_delete=models.SET_NULL, related_name='operator_sample', null=True)

    class Meta:
        indexes = [
            models.Index(fields=['operator_id'], name='operator_id_idx')
        ]


class SampleSerializer(serializers.ModelSerializer):
    batch = ImageBatchSerializer()
    patient = PatientSerializer(allow_null=True, required=False)
    operator_detail = OperatorSerializer(source='operator_id', allow_null=True, read_only=True)

    class Meta:
        model = Sample
        fields = '__all__'

    def create(self, validated_data):
        batch_data = validated_data.pop('batch')
        batch = ImageBatch.objects.create()
        for image in batch_data['images']:
            batch.images.create(**image)
        patient = validated_data.pop('patient',None)
        if patient:
            address = patient.pop('address', None)
            if address:
                address = Address.objects.create(**address)
            patient = Patient.objects.create(address=address, **patient)

        return Sample.objects.create(batch=batch, patient=patient, **validated_data)


class SampleReview(BaseModel):
    sample_id = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name='sample_reviews', null=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, related_name='doctor_reviewed_sample', null=True)
    review = models.TextField(null=True)
    again_review = models.BooleanField(null=True, default=False)
    images_unclear = models.BooleanField(null=True, default=False)

    class Meta:
        indexes = [
            models.Index(fields=['sample_id'], name='sample_id_idx'),
            models.Index(fields=['doctor_id'], name='doctor_id_idx'),
        ]


class SampleReviewSerializer(serializers.ModelSerializer):
    sample_detail = SampleSerializer(source='sample_id', read_only=True)
    doctor_detail = DoctorSerializer(source='doctor_id', read_only=True, allow_null=True)

    class Meta:
        model = SampleReview
        fields = '__all__'


class SampleComment(BaseModel):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['sample'], name='sample_idx'),
            models.Index(fields=['comment_by'], name='comment_by_idx'),
        ]


class SampleCommentSerializer(serializers.ModelSerializer):
    comment_by_detail = UserSerializer(read_only=True)

    class Meta:
        model = SampleComment
        fields = '__all__'
