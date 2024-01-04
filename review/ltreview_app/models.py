from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='Description par défaut')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    # Utilisateur qui suit
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')

    # Utilisateur suivi
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        # Assure qu'un utilisateur ne peut suivre un autre utilisateur qu'une seule fois
        unique_together = ('user', 'followed_user')

class CustomUser(AbstractUser):
    # Champ supplémentaire : livre préféré de l'utilisateur
    # favorite_book = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username


