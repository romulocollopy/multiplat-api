from django.urls import path

from . import views
from .schema import user_schema

urlpatterns = [
    path("", views.HomeView.as_view(graphiql=True, schema=user_schema)),
    path("csrf_token/", views.CSRFView.as_view()),
]
