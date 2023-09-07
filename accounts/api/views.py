from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status


class UserCreateApi(APIView):

    def post(self,request):

        try:
            data = request.data
            serializer = UserSerializer(data=data)

            if not serializer.is_valid():            
                response = {
                     'data' : serializer.errors,
                     'msg' : 'serilaization data is not valid'
                 }
                return Response(response,status=status.HTTP_406_NOT_ACCEPTABLE)

            serializer.save()
            response = {
                    'data': [serializer.data],
                    'msg' : 'User created'
                }
            return Response(response,status=status.HTTP_201_CREATED)
            
        except Exception as e:

            return Response({'exception error' : e},status=status.HTTP_400_BAD_REQUEST)
        

class LoginApi(APIView):
    
    def post(self,request):

        try:
            data = request.data
            serializer = LoginSerializer(data=data)

            if serializer.is_valid():
                response = serializer.get_jwt_token(serializer.data)


                return Response(response,status=status.HTTP_302_FOUND)

            else:
                response = {
                    'data' : [serializer.errors],
                    'msg' : 'serilaization data is not valid'
                }
                return Response(response,status=status.HTTP_404_NOT_FOUND)


        except Exception as e:
            return Response({"exception error" : e}, status=status.HTTP_400_BAD_REQUEST)