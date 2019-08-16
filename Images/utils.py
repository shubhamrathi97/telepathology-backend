import boto3
from django.conf import settings
from botocore.client import Config
import base64

boto_conn = boto3.client('s3',
                                 region_name=settings.AWS_S3_REGION,
                                 aws_access_key_id=settings.AWS_ACCESS_KEY,
                                 aws_secret_access_key=settings.AWS_SECRET_KEY,
                                 # config=Config(signature_version='s3v4')
)


def get_presigned_url(key):
    s3_key = settings.S3_ENV + '/image/' + str(key)
    # resp = boto_conn.generate_presigned_url(
    #         'put_object',
    #         Params={'Bucket': settings.BUCKET_NAME,
    #                 'Key': str(s3_key),
    #                 # 'ACL':'public-read'
    #                 'ContentType': 'image/png',
    #                 },
    #         ExpiresIn=3600)
    resp = boto_conn.generate_presigned_post(settings.BUCKET_NAME, s3_key)
    return {'result': 'success',
            'data': {'uploadURL': resp,
                     'key': s3_key + '.png',
                     'callbackUrl': '/images/set_upload_public/?key={}'.format(s3_key)}}


def set_s3_key_public(key):
    boto_conn.put_object_acl(ACL='public-read',
                                             Bucket=settings.BUCKET_NAME,
                                             Key=key)
    return {'result':'success','data':''}


def upload_file(base64_string, key):
    base64_type, base64_string = base64_string.split(';')
    base64_type = base64_type.split('/')[1]
    base64_string = base64_string.split(',')[1]
    key = settings.S3_ENV + '/image/' + str(key)

    response = boto_conn.put_object(
        ACL='public-read',
        Body= base64.b64decode(base64_string),
        Bucket= settings.BUCKET_NAME,
        ContentEncoding='base64',
        ContentType='image/{}'.format(base64_type),
        Key=key,
    )

    url = "https://{}.s3.ap-south-1.amazonaws.com/{}".format(settings.BUCKET_NAME, key)
    return {'result':'success', 'data':{'url':url}}