from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError(f"{data['email']} is already exist")

        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError(f"{data['username']} is already exist")
        
        username = data['username']
        password = data['password']

        if username == password:
            raise serializers.ValidationError("password and username should not be same")
        
        if len(password) < 8:
            raise serializers.ValidationError(f"password length is {len(password)} . It should be minimum 8 length")
        
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'].lower(),
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        user.set_password(validated_data["password"])
        user.save()

        return validated_data
    

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()


    def validate(self, data):
        if not User.objects.filter(username = data['username'].lower()).exists():
            return serializers.ValidationError("data not found")
        
        return data
    
    def get_jwt_token(self,data):

        user = authenticate( username = data['username'] , password = data['password'])
        if not user:
            return {'msg' : 'invalid credentials', 'data' : data}

        refresh = RefreshToken.for_user(user)

        return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
}
    