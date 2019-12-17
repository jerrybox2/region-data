from django.urls import path

from .views import get_region


urlpatterns = [
    path(r'<str:grade>/<int:deepth>', get_region),
]
