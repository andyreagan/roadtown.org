# views.py
from django.shortcuts import redirect


def home(_):
    return redirect("/trot/", permanent=False)


def quarters2025(_):
    return redirect(
        "https://app.acuityscheduling.com/schedule/99a07fbd/?appointmentTypeIds[]=40291455",
        permanent=True,
    )
