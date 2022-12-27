from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from encroachment_app.adapters import views

router = routers.DefaultRouter()

router.register(r'encroachment', views.EncroachmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(router.urls)),
    # path('api-auth',include('rest_framework.urls',namespace='rest_framework'))
]