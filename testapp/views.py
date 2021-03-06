from .models import User
from rest_framework import viewsets
from rest_framework import permissions, generics
from .serializers import UserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignupView(APIView):
    def post(self, request):
        user = User.objects.create_user(nickname=request.data['nickname'], password=request.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key, "User": user.nickname})

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = Token.objects.get(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })