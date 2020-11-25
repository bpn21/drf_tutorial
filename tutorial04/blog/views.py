from .models import Post,Category
from .serializers import PostSerializer,CategorySerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class PostList(APIView):
    """
    List all code post, or create a new post.
    """

    def get(self, request,format=None):
        print('request.data is : ',request.data)  
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)    

    def post(self,request,format=None):
        print('request.data is : ',request.data)  
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PostDetail(APIView):
    """
    Retrieve, update or delete a code post.
    """
    def get_object(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            return Post.objects.get(pk=pk)
        except post.DoesNotExist:
            return Response(status=404)

    def get(self,request,pk,format=None):
        print('request.data is : ',request.data)  
        print('request.method is : ',request.method)  
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        print('serializer.data is : ',serializer.data)  
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        print('request.method is : ',request.data)  
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self,request,pk,format=None):
        print('request.method is : ',request.data)  
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        post.delete()
        return Response(serializer.data)
        return HttpResponse(status=204)

