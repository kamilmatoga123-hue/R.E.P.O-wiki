from django.db import models

class Item(models.Model):
    ITEM_TYPES = [
        ("weapon", "Weapon"),
        ("tool", "Tool"),
        ("upgrade", "Upgrade"),
        ("consumable", "Consumable"),
    ]
    name = models.CharField(max_length=100, default="")
    item_type = models.CharField(max_length=50, choices=ITEM_TYPES, default="tool") # Zmieniłem nazwę z 'type', bo to słowo kluczowe w Pythonie
    value = models.CharField(default="") # Zmienione na Integer
    effect = models.TextField(null=True, blank=True, default="")
    image_path = models.CharField(max_length=200, null=True, blank=True, default="")

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    location_type = models.CharField(max_length=100, default="") 
    image_path = models.CharField(max_length=200, null=True, blank=True, default="")

    def __str__(self):
        return self.name


class GameLore(models.Model):
    title = models.CharField(max_length=200, default="")
    content = models.TextField(default="")

    class Meta:
        verbose_name_plural = "Game Lores"

    def __str__(self):
        return self.title


class Monster(models.Model):
    name = models.CharField(max_length=100, default="")
    health = models.IntegerField(default=0) 
    damage = models.IntegerField(default=0) 
    danger = models.IntegerField(default=0)
    image_path = models.CharField(max_length=200, null=True, blank=True, default="")

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    image_path = models.CharField(max_length=200, null=True, blank=True, default="")
    
    def __str__(self):
        return self.name

class Valuable(models.Model):
    name = models.CharField(max_length=100, default="")
    size = models.CharField(default=0) 
    value = models.CharField(default=0) 
    place = models.CharField(max_length=100, default="")
    image_path = models.CharField(max_length=200, null=True, blank=True, default="")

    def __str__(self):
        return self.name