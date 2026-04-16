from django.shortcuts import render
from .models import Item, Location, GameLore, Monster, Player, Valuable

def info_items(request):
    items = Item.objects.all()
    return render(request, "info/info_items.html", {"items": items})

def info_locations(request):
    locations = Location.objects.all()
    return render(request, "info/info_locations.html", {"locations": locations})

def info_lore(request):
    lores = GameLore.objects.all()
    return render(request, "info/info_lore.html", {"lores": lores})

def info_moby(request):
    monsters = Monster.objects.all()
    return render(request, "info/info_moby.html", {"monsters": monsters})

def info_value(request):
    valuables = Valuable.objects.all()
    return render(request, "info/info_value.html", {"valuables": valuables})

def info_player(request):
    players = Player.objects.all()
    return render(request, "info/info_player.html", {"players": players})
def info(request):
    return render(request, 'info/info.html')
