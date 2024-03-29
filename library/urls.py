from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/",views.ResultsView.as_view(), name="results"),
    path("<int:library>/vote/", views.vote, name="vote"),
    path("new_book/", views.new_question, name="new_question")
]
