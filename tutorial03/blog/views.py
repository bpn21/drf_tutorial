from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Post,Category
from .serializers import PostSerializer,CategorySerializer

@csrf_exempt  # post garna parcha so.. kai data post garda csrf of error naos bhaneyra rakheko
def post_list(request):
    """
    List all code post, or create a new post.
    """
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def post_detail(request, pk):
    """
    Retrieve, update or delete a code post.
    """
    try:
        post = Post.objects.get(pk=pk)
    except post.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        serializer = PostSerializer(post)
        post.delete()
        return JsonResponse(serializer.data)
        return HttpResponse(status=204)

