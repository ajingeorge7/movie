from.import views
from django.urls import path
from .views import add_movie

app_name='jhons'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/<int:movie_id>/',views.add_movie,name='add_movie'),
    path('add/', add_movie, name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
