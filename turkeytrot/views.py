from django.template.response import TemplateResponse


def trot_main_page(request):
    return TemplateResponse(request, "trot2025bootstrap.html", {})


def trot_past_years(request, year):
    return TemplateResponse(request, f"trot{year}bootstrap.html", {})
