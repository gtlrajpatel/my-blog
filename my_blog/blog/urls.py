from django.urls import path, include
from .views import BlogListView, ProfileView, NewBlogView, BlogDeleteView, BlogUpdateView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('create/', NewBlogView.as_view(success_url="/"), name='create_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='post-delete'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='post-update'),
    path('search/', views.search, name='search'),

]
