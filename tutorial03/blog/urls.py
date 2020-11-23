from .views import  post_list,post_detail

from django.urls import path,include
urlpatterns = [
    path('',post_list,name = "list"),
    path('<int:pk>/',post_detail)
]
