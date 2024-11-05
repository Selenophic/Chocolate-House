from django.contrib import admin
from .models import Chocolate, SeasonalFlavor, Ingredient, CustomerSuggestion

admin.site.register(Chocolate)
admin.site.register(SeasonalFlavor)
admin.site.register(Ingredient)
admin.site.register(CustomerSuggestion)
