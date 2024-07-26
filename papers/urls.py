from .views import *
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Referto API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url='https://referto-backend.fly.dev',  # URL을 HTTPS로 설정합니다.
)

urlpatterns = [
    path('', PaperUploadView.as_view(), name='paper-upload'),
    path('<int:pk>/', PaperDetailView.as_view(), name='paper-detail'),
    path('<int:pk>/number/', PaperNumberView.as_view(), name='paper-number'),
]