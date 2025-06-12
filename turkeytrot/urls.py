from django.urls import path

from .views import trot_main_page, trot_past_years

urlpatterns = [
    path("", trot_main_page, name="main"),
    path("<int:year>/", trot_past_years, name="past"),
]
