from django.db import models

# definir la structure du produits
class Tag(models.Model):
    nom = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prix = models.IntegerField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self): # permet d'afficxher le nom de produit
        return self.nom


