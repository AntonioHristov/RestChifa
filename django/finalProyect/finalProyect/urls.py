from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('restChifa/', include('restChifa.urls')),
    path('admin/', admin.site.urls),
]