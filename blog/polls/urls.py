'''import ur url here
'''
from django.conf.urls import url 
from . import views


app_name='polls'

urlpatterns = [
    # method 1
    #url(r'^index/',views.index.as_view(), name='index'), # ex: /polls/index
    url(r'^index/', views.index, name='index'),    #/polls/index
    url(r'^choice/', views.pilihan, name='pilihan'),
    url(r'^(?P<question_id>[0-9]+)/$', views.question_details, name='question_detail'),
    #url(r'^details/', views.question_details, name='question_details'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'), # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.vote, name='vote_s'),
    url(r'^(?P<question_id>[0-9]+)/$', views.result, name='result'),
]