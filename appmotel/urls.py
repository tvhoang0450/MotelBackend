from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('authgg/', include('rest_framework_social_oauth2.urls')),
    path('PhongTro/', include("motel.urls")),
    path('', include("profile_user.urls")),
]
