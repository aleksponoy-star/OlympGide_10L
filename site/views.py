from django.shortcuts import render
from core.models import OlympNapr

def index(request):
    return render(request, "default.html")


def olymp_napr_list(request):
    items = OlympNapr.objects.select_related(
        "olympiad", "profil", "predmet", "level"
    ).order_by(
        "profil__name",          
        "level__name",          
        "predmet__name",         
        "olympiad__full_name"    
    )

    return render(request, "olymp_napr_list.html", {
        "items": items
    })



