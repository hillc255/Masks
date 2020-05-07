from django.urls import path

from . import views

urlpatterns = [
        # ex: /masks/
        path('', views.index, name='index'),
        # ex: /masks/5/
        path('<int:title_id>/', views.detail, name='detail'),
        # ex: /polls/5/results/
        path('<int:title_id>/results/', views.results, name='results'),
        # ex: /title/5/vote/
        path('<int:title_id>/vote/', views.vote, name='vote'),

    ]
