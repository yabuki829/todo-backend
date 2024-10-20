from django.contrib.auth import login,logout
from rest_framework import generics,views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import LoginSerializer

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    
    def post(self,request, *args, **kwargs):
        print('ログインします')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        print(serializer.validated_data)

        user = serializer.validated_data["user"]
        
        login(request,user)

        return Response({'detai':'ログインが成功しました。'})
    
    def get(self,request, *args, **kwargs):
        return Response({'detail':'ログインが成功しました。'})


    

class LogoutView(views.APIView):
    def post(self,request, *args, **kwargs):
        logout(request)
        return Response({'detail':'ログアウトが成功しました。'})