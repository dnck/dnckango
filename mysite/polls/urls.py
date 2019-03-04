from django.urls import path
from . import views
app_name = 'polls'
# path(route, view, kwargs, name)
urlpatterns = [path('', views.index, name='index'),
                path('zoofun/', views.zoofun, {'censor': True}, name='zoofun'),
                path('<int:question_id>/', views.detail, name='detail'),
                path('<int:question_id>/results/', views.results, name='results'),
                path('<int:question_id>/vote/', views.vote, name='vote'),
                path('holyshit/', views.holyshit, name='holyshit'),
                ]
