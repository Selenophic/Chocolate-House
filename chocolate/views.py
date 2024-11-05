from django.shortcuts import render, redirect
from .models import Chocolate, SeasonalFlavor, Ingredient, CustomerSuggestion

def index(request):
    chocolates = Chocolate.objects.all()
    return render(request, 'index.html', {'chocolates': chocolates})

def add_chocolate(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Chocolate.objects.create(name=name, description=description)
        return redirect('index')
    return render(request, 'add_chocolate.html')

def add_flavor(request, chocolate_id):
    chocolate = Chocolate.objects.get(id=chocolate_id)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        availability = request.POST['availability']
        SeasonalFlavor.objects.create(chocolate=chocolate, name=name, description=description, availability=availability)
        return redirect('view_entries', chocolate_id=chocolate_id)
    return render(request, 'add_flavor.html', {'chocolate': chocolate})

def add_ingredient(request, chocolate_id):
    chocolate = Chocolate.objects.get(id=chocolate_id)
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        unit = request.POST['unit']
        Ingredient.objects.create(chocolate=chocolate, name=name, quantity=quantity, unit=unit)
        return redirect('view_entries', chocolate_id=chocolate_id)
    return render(request, 'add_ingredient.html', {'chocolate': chocolate})

def add_suggestion(request, chocolate_id):
    chocolate = Chocolate.objects.get(id=chocolate_id)
    if request.method == 'POST':
        flavor_suggestion = request.POST['flavor_suggestion']
        customer_name = request.POST['customer_name']
        allergy_concerns = request.POST['allergy_concerns']
        CustomerSuggestion.objects.create(
            chocolate=chocolate,
            flavor_suggestion=flavor_suggestion,
            customer_name=customer_name,
            allergy_concerns=allergy_concerns
        )
        return redirect('view_entries', chocolate_id=chocolate_id)
    return render(request, 'add_suggestion.html', {'chocolate': chocolate})

def view_entries(request, chocolate_id):
    chocolate = Chocolate.objects.get(id=chocolate_id)
    flavors = chocolate.seasonal_flavors.all()
    ingredients = chocolate.ingredients.all()
    suggestions = chocolate.suggestions.all()

    context = {
        'chocolate': chocolate,
        'flavors': flavors,
        'ingredients': ingredients,
        'suggestions': suggestions
    }
    return render(request, 'view_entries.html', context)

