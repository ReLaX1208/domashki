from django.urls import path, re_path

from bboard.models import Bb
from bboard.views import (index, BbCreateView,
                          BbByRubricView, BbDetailView,
                          BbDeleteView, BbRedirectView, edit, RubCreateView, rubrics, about,
                          edit_rubric, RubricDeleteView, Search, api_rubrics, api_rubric_detail, UserCreateView, )

app_name = 'bboard'

urlpatterns = [
    path('api/rubrics/<int:pk>/', api_rubric_detail),
    path('api/rubrics/', api_rubrics),
    path('add/', BbCreateView.as_view(), name='add'),
    path('update/<int:pk>/', edit, name='update'),
    path('rubrics/<int:pk>/edit/', edit_rubric, name='edit_rubric'),
    path('rubrics/<int:pk>/delete/', RubricDeleteView.as_view(), name='delete_rubric'),
    path('addrub/', RubCreateView.as_view(), name='addrub'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('detail/<int:year>/<int:month>/<int:day>/<int:pk>/',
         BbRedirectView.as_view(), name='old_detail'),
    path('rubrics/', rubrics, name='rubrics'),
    path('', index, name='index'),
    path('search/', Search.as_view(), name='search'),
    path('about/', about, name='about'),
    path('register/', UserCreateView.as_view(), name='user-register'),
]
