from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
import uuid
from . import utils


class GetUploadURL(generics.ListAPIView):
    permission_classes = ()
    def get(self, request, *args, **kwargs):
        key = request.GET.get('key',uuid.uuid4())
        res = utils.get_presigned_url(key)
        return Response(res)


class SetURLPublic(generics.ListAPIView):
    permission_classes = ()
    def get(self, request, *args, **kwargs):
        key = request.GET.get('key',None)
        if key is None:
            return Response({'result':'error', 'data': 'Key is Missing'})
        res = utils.set_s3_key_public(key)
        return Response(res)


class UploadImage(generics.CreateAPIView):
    permission_classes = ()
    def post(self, request, *args, **kwargs):
        data = request.data
        base64_string = request.data.get('base64')
        if not base64_string:
            return Response({'result':'error','message':'Image value missing'})
        key = request.GET.get('key', uuid.uuid4())
        res = utils.upload_file(base64_string, key)
        return Response(res)