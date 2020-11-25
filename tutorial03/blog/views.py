from .models import Post,Category
from .serializers import PostSerializer,CategorySerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def post_list(request,format = None):
    """
    List all code post, or create a new post.
    """
    print('request is : ',request)
    print('request.method is : ',request.method)
    print('request.method is : ',request.data)


    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)    

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = PostSerializer(data=data)
        serializer = PostSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET','PUT','DELETE'])
def post_detail(request, pk,format = None):
    """
    Retrieve, update or delete a code post.
    """
    try:
        post = Post.objects.get(pk=pk)
    except post.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        serializer = PostSerializer(post)
        post.delete()
        return Response(serializer.data)
        return HttpResponse(status=204)

