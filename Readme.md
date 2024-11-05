A simple Django-based web application to manage seasonal flavor offers, 
ingredient inventory, customer feedback (suggestions and allergy concerns) for chocolate. 
The database used is SQLite to access and store information of different kinds of chocolates, 
flavors, ingredients, and customer inputs.

Features
* Seasonal Flavor Offerings: Gives their flavor and  seasonal availability.
* Ingredient Inventory: Gives ingredients and quantities needed for each chocolate.
* Customer Suggestions: Add customer suggestions for chocolate enhancements or to get new flavors.
* Allergy Concerns: Store and manage customer allergy concerns related to each chocolate.


Installation and Setup

Prerequisites
  Python 3.x
  Django 4.x

Steps
1. Clone the Repository
        Clone the project repository to your local machine.
2. Set Up the Database : Django uses SQLite by default. Run the following commands to create the database and apply migrations.


      python manage.py makemigrations
      python manage.py migrate

3. Create a Superuser : To access the Django admin interface, create a superuser account.

      python manage.py createsuperuser

4. Run the Server : Start the Django development server.
      python manage.py runserver

5. Open the application in a browser at http://127.0.0.1:8000.     

Application Structure

The project is structured as follows:

  chocolate_house_project/: The main project folder.
   chocolate_house/: The main app that includes views, models, forms, and templates.
   templates/chocolate_house/: HTML templates for displaying data and forms.
   models.py: Contains the data models for Seasonal Flavors, Ingredients, and Customer Suggestions.
   views.py: Contains the logic for handling requests and rendering responses.
   forms.py : Contains form classes for user input.


Models

SeasonalFlavor

Fields
   flavor_name: Name of the flavor (e.g., "Pumpkin Spice").
   description: Description of the flavor.
   available_from: Date when the flavor becomes available.
   available_until: Date when the flavor is no longer available.

Ingredient

Fields
    ingredient_name: Name of the ingredient (e.g., "Cocoa").
    quantity_in_stock: Quantity in stock.
    unit: Unit of measurement (e.g., "kg", "L").

CustomerSuggestion

Fields
  customer_name: Name of the customer submitting the suggestion.
  flavor_suggestion: Suggested flavor.
  allergy_concern: Any allergy concerns related to the suggestion.

Usage

Home Page: Links to view seasonal flavors, ingredient inventory, and customer suggestions.
Seasonal Flavors:
    View available seasonal flavors.
    Add new flavors with a name, description, and availability dates.

Ingredient Inventory:
    View ingredient quantities and add new ingredients to inventory.

Customer Suggestions:
    View customer suggestions for new flavors and related allergy concerns.
    Add new customer suggestions.

Built with Django, an open-source web framework.

