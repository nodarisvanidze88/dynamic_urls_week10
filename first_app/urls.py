from django.urls import path
from .views import index, show_item
urlpatterns = [
    path("test/", index),
    path("test/<int:id>", show_item)
]
