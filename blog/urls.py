from django.urls import path
from blog import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('category/<str:slug>', views.CategoryView.as_view(), name='category'),
    path('posts/<str:slug>', views.PostsViews.as_view(), name='posts'),
    path('tags/<str:slug>', views.TagsViews.as_view(), name='tags'),
    path('search/', views.SearchView.as_view(), name='search')
]
