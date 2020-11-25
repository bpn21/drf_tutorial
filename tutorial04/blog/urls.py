from .views import  PostList,PostDetail
from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path,include
urlpatterns = [
    path('all',PostList.as_view(),name = "list"),
    path('<int:pk>/',PostDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)