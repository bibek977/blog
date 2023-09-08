from rest_framework.response import Response
from rest_framework import views
from .serializers import *
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from core.models import Blog

class ShowApi(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer


class BlogApi(views.APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self,request):

        data = request.data
        data['author'] = request.user.id
        serializer = BlogModelSerializer(data = data)

        if not serializer.is_valid():
            response = {
                'error' : serializer.errors,
                "msg" : "validation error"
            }

            return Response(response,status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        

        serializer.save()

        response = {
            'success' : serializer.data,
            'msg' : "post created"
        }

        return Response(response,status=status.HTTP_201_CREATED)