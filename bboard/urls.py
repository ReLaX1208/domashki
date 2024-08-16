from django.urls import path, re_path, include

import testapp
from .views import index, by_rubric, BbCreateView, add_and_save, UserController, user_form

app_name = 'bboard'


urlpatterns = [
    path('users/', UserController.as_view()),
    path('users/<int:pk>/', UserController.as_view()),
    path('user_form/', user_form, name='user_form'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('add/', add_and_save, name='add'),
]
