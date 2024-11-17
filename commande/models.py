from django.db import models

from client.models import Client
from produit.models import Produit


# Create your models here.
class Commande(models.Model):
    STATUS=(("en instance", "en instance"),("non livré", "non livré"),("livré", "livré"))
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True)
    status  = models.CharField(max_length=200, choices=STATUS)
    date_creation = models.DateTimeField(auto_now_add=True)
