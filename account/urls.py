from django.contrib.auth import views as auth_views
from . import views
from django.urls import path


urlpatterns = [
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('test/', views.test, name='test'),
    # path('test1/', views.test1, name='test1'),



]