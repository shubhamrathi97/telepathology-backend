from backend.models import BaseModel, models
from User.models import User
from rest_framework import serializers


class Image(BaseModel):
    url = models.URLField()


class ImageBatch(BaseModel):
    images = models.ManyToManyField(Image, related_name='image_batch', blank=True)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ImageBatchSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, allow_null=True)

    class Meta:
        model = ImageBatch
        fields = '__all__'

    def create(self, validated_data):
        batch = ImageBatch.objects.create()
        images = validated_data.pop('images')
        for image in images:
            batch.images.create(**image)
        batch.save()
        return batch

