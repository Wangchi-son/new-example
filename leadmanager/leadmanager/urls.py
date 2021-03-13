# 쟝고로 작성된 사이트들의 목차(경로)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('surveys.urls')),
]
