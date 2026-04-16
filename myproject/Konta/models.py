from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Zamiast encrypt(), używamy zwykłego pola, 
    # a szyfrowanie zrobimy "ręcznie" w logice, jeśli będzie potrzebne.
    pesel = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username