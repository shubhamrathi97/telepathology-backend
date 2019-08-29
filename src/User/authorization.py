from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_auth.views import LoginView
from User.models import CustomUserDetailsSerializer
from rest_framework.authentication import TokenAuthentication


class CustomAuthToken(LoginView):
    permission_classes = ()
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['key'])
        user = CustomUserDetailsSerializer(token.user).data
        # if user['type'] == 'admin':
        return Response({'token': token.key, 'user': CustomUserDetailsSerializer(token.user).data})
        # if user['type'] == 'Patient':
        #     return Response({'Message':'Not Allowed'}), 400
        # return Response({'token': token.key, 'user': CustomUserDetailsSerializer(token.user).data, 'user_permission':HospitalStaffSerializer(user_permission).data})
