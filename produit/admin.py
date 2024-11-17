from django.contrib import admin
from .models import Produit
from .models import Tag

# Register your models here.
admin.site.register(Produit) # permet dafficher dans la base de donnes et enregistrer
admin.site.register(Tag)