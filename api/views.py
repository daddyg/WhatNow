from django.shortcuts import render
from django.http import Http404
from django.utils.translation import gettext_lazy as _

from .models import Sports

# Create your views here.

def index(request):
    available_sports = Sports.choices
    
    context = { 'available_sports': available_sports }

    return render(request, "index.html", context)

# Sport

def sportDetail(request, sport_name):
    try:
        sport = Sports(sport_name)
    except Exception:
        raise Http404(_("This sport was not understood"))
    
    return render(request, "sport/detail.html", {"sport": sport})