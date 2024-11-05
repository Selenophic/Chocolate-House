from django.urls import path
from .views import index, add_chocolate, add_flavor, add_ingredient, add_suggestion, view_entries

urlpatterns = [
    path('', index, name='index'),
    path('add_chocolate/', add_chocolate, name='add_chocolate'),
    path('add_flavor/<int:chocolate_id>/', add_flavor, name='add_flavor'),
    path('add_ingredient/<int:chocolate_id>/', add_ingredient, name='add_ingredient'),
    path('add_suggestion/<int:chocolate_id>/', add_suggestion, name='add_suggestion'),
    path('view/<int:chocolate_id>/', view_entries, name='view_entries'),
]
