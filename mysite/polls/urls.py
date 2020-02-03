from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('suggestions/', views.addSuggestion, name='suggestion'),
    # path('suggestions/', views.SuggestionView.as_view(), name='suggestion'),

    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
]