from django.urls import path
from django.shortcuts import redirect
from django.http import Http404


def trot_main_redirect(request):
    """Redirect /trot/ to the current year's page (homepage)"""
    return redirect("/", permanent=True)


def trot_year_redirect(request, year):
    """Redirect /trot/YEAR/ to Wagtail pages"""
    if year == 2025:
        return redirect("/", permanent=True)  # Current year is homepage
    elif year in [2023, 2024]:
        # Try to find the specific year page in Wagtail
        try:
            from .models import TurkeyTrotPage

            page = TurkeyTrotPage.objects.filter(slug__icontains=str(year)).first()
            if page:
                return redirect(page.url, permanent=True)
        except:
            pass
        # Fallback to homepage
        return redirect("/", permanent=True)
    else:
        raise Http404("Year not found")


urlpatterns = [
    path("", trot_main_redirect, name="main"),
    path("<int:year>/", trot_year_redirect, name="past"),
]
