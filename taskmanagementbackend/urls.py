
from django.contrib import admin
from django.urls import path
from authToken.views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]

