import jwt
from django.contrib.auth import user_logged_in
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler

from todo_app.settings import SECRET_KEY
from .models import User
from .serializers import UserDetailSerializer, UserAuthenticateSerializer


class RegisterUserView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserDetailSerializer


class EditUserView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = UserDetailSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthenticateUserView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserAuthenticateSerializer

    def post(self, request, organization='', *args, **kwargs):
        try:
            email = request.data['email']
            password = request.data['password']

            user = User.objects.get(email=email, password=password)
            if user:
                try:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, SECRET_KEY)
                    user_details = {'name': "%s %s" % (
                        user.first_name, user.last_name
                    ), 'token': token, 'organization': organization}
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)
                    return Response(user_details, status=status.HTTP_200_OK)
                except Exception as e:
                    raise e

            else:
                res = {
                    'error': 'Can not authenticate with the given credentials or the account has been deactivated'
                }
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            res = {'error': 'Please provide an email and a password'}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
