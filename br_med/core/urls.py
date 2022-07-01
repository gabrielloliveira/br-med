from django.urls import path

from . import views
from .viewsets import QuoteListView

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/v1/quotes/", QuoteListView.as_view(), name="api-quote-list"),
]
