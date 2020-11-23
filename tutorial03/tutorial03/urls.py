from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('post/',include('blog.urls')),
    path('admin/', admin.site.urls)
]
