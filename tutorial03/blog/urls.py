from .views import  post_list,post_detail
from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path,include
urlpatterns = [
    path('all',post_list,name = "list"),
    path('<int:pk>/',post_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)