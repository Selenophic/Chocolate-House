from django.db import models

class Chocolate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class SeasonalFlavor(models.Model):
    chocolate = models.ForeignKey(Chocolate, on_delete=models.CASCADE, related_name='seasonal_flavors')
    name = models.CharField(max_length=100)
    description = models.TextField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.chocolate.name})"

class Ingredient(models.Model):
    chocolate = models.ForeignKey(Chocolate, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.chocolate.name})"

class CustomerSuggestion(models.Model):
    chocolate = models.ForeignKey(Chocolate, on_delete=models.CASCADE, related_name='suggestions')
    flavor_suggestion = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100, blank=True)
    allergy_concerns = models.TextField(blank=True)

    def __str__(self):
        return f"{self.flavor_suggestion} for {self.chocolate.name}"

