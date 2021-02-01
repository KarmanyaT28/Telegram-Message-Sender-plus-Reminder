from django.urls import path
from . import views
from .views import HomeView , PostView ,ManagePostView,CreatePostView,UpdatePostView,DeletePostView,postmess , sendmess 

urlpatterns = [

    # path('',views.home,name="home"),
    path('',HomeView.as_view(),name="first"),
    path('post/<int:pk>',PostView.as_view(),name="details"),
    path('manage/',ManagePostView.as_view(),name="home"),
    path('create/',CreatePostView.as_view(),name="create"),
    path('post/edit/<int:pk>',UpdatePostView.as_view(),name="update"),
    path('post/<int:pk>/remove',DeletePostView.as_view(),name="delete"),
    path('posted/',views.postmess,name="posted"),
    path('send/',views.sendmess,name="send"),
    

]
