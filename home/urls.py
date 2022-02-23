from django.contrib.auth import views as auth_views
from home import views
from home.views import * 

from django.urls import path


urlpatterns = [
     path('home/', views.home, name='home'),
     path('post/', views.posting , name='posting'),
     path('edit_post/<int:post_id>',views.edit_post,name="edit_post"),
     path('update_post/<int:post_id>',views.update_post,name="update_post")




]