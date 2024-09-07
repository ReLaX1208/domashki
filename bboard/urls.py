from django.urls import path, re_path, include

import testapp
from .views import index, by_rubric, BbCreateView, add_and_save, my_controller

app_name = 'bboard'


urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('add/', add_and_save, name='add'),
    path('da/', my_controller, name='da'),
]
