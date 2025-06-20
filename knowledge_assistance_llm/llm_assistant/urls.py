from django.urls import path
from .views import AskQuestionView

urlpatterns = [
    path("ask-question/", AskQuestionView.as_view()),
]
