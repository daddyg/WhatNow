from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Sports(models.TextChoices):
    RUNNING = "RUNNING", _("Running")
    SURFING = "SURFING", _("Surfing")
    TRAIL_RUNNING = "TRAIL_RUNNING", _("Trail Running")
    WALKING = "WALKING", _("Walking")
    WIND_SURFING = "WIND_SURFING", _("Wind Surfing")

class UserSport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.CharField(max_length=100, choices=Sports.choices)
