from rest_framework.response import Response
from rest_framework import views
from .serializers import *
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from core.models import Blog
from django.db.models import Q

class ShowApi(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer


class BlogApi(views.APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request):
        
        blog = Blog.objects.filter(author = request.user)

        if request.GET.get('search'):
            search = request.GET.get('search')
            blog = blog.filter(Q(description__icontains = search | Q(title__icontains = search)))

        serializer = BlogModelSerializer(blog, many=True)
        response = {
            'data' : serializer.data,
            "msg" : f"All Blogs of {request.user}"
        }
        return Response(response,status=status.HTTP_302_FOUND)

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

    def patch(self,request):

        data = request.data

        blog = Blog.objects.filter(id = data.get('id'))

        if not blog.exists():
            response = {
                'error' : "Not a valid blog id",
                'msg' : "blog id should be valid"
            }
            return Response(response,status=status.HTTP_401_UNAUTHORIZED)            

        if request.user != blog[0].author:
            response = {
                'error' : "Not a valid user",
                'msg' : "user should be valid"
            }
            return Response(response,status=status.HTTP_401_UNAUTHORIZED)

        serializer = BlogModelSerializer(blog[0],data=data,partial=True)


        if not serializer.is_valid():
            response = {
                'error' : serializer.errors,
                "msg" : "validation error"
            }

            return Response(response,status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        serializer.save()

        response = {
            'success' : serializer.data,
            'msg' : "data updated"
        }

        return Response(response,status=status.HTTP_206_PARTIAL_CONTENT)

    
    def delete(self,request):

        data = request.data

        blog = Blog.objects.filter(id = data.get('id'))

        if not blog.exists():
            response = {
                'error' : "Not a valid blog id",
                'msg' : "blog id should be valid"
            }
            return Response(response,status=status.HTTP_401_UNAUTHORIZED)            

        if request.user != blog[0].author:
            response = {
                'error' : "Not a valid user",
                'msg' : "user should be valid"
            }
            return Response(response,status=status.HTTP_401_UNAUTHORIZED)

        blog[0].delete()

        response = {
            'data' : {},
            'msg' : "blog is deleted"
        }
        return Response(response,status=status.HTTP_401_UNAUTHORIZED)       