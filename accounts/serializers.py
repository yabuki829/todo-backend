from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True,style={"input_type":"password"})

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password :
            user = authenticate(request=self.context.get('request'),email=email,password=password)

            if user is None or not user.is_active :
                raise serializers.ValidationError("ログインが失敗しました。")
        
            data['user'] = user
        return data
    
