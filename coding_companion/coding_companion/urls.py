from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include("userprofile.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/problems/', include('problem.urls')),
    re_path(r'^login/$', views.LoginView.as_view(
        template_name='rest_framework/login.html'), name='login'),
    re_path(r'^logout/$', views.LogoutView.as_view(), name='logout'),

]
