from django.urls import path, re_path, include

import testapp
from bboard.views import index, by_rubric, BbCreateView


app_name = 'bboard'

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]
