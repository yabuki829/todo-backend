from django.contrib.auth import login,logout
from rest_framework import generics,views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import LoginSerializer


# セッション
class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    
    def post(self,request, *args, **kwargs):
        print('ログインします')
       
        if request.user.is_authenticated:
            print("ログインしています")
            return Response({'detail':'ログインしています'})
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)

        user = serializer.validated_data["user"]
        
        login(request,user)
        return Response({'detai':'ログインが成功しました。'})
    
    def get(self,request, *args, **kwargs):
        print("--------------------------------")
        print(request)
        print(request.user)
        print(request.user.is_authenticated)
        print(request.session)
        print("--------------------------------")

        if request.user.is_authenticated:
            print("ログインしています")
            return Response({'detail':'ログインしています'})
        else:
            print("ログインしていません")
            return Response({'detail':'ログインして下さい。'})

class LogoutView(views.APIView):
    def post(self,request, *args, **kwargs):
        logout(request)
        return Response({'detail':'ログアウトが成功しました。'})
    


# https://stackoverflow.com/questions/53270326/request-user-is-authenticated-is-always-false-in-django-rest-framework   