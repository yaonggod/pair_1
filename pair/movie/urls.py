from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:movie_pk>', views.detail, name="detail"),
    path('delete/<int:movie_pk>', views.delete, name='delete'),
    path('edit/<int:movie_pk>', views.edit, name='edit'),
    path('update/<int:movie_pk>', views.update, name='update'),
]