# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object



# class CarMake(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField()
#     country = models.CharField(max_length=100, blank=True, null=True)  # Optional: country of origin
#     founded_year = models.PositiveIntegerField(blank=True, null=True)  # Optional: year founded

#     def __str__(self):
#         return f"{self.name} - {self.country if self.country else 'N/A'}"


# from django.db import models
# from .models import CarMake  # Ensure CarMake is in the same app or import properly

# class CarModel(models.Model):
#     # Define choices for car type
#     SEDAN = 'Sedan'
#     SUV = 'SUV'
#     WAGON = 'Wagon'
#     COUPE = 'Coupe'
#     HATCHBACK = 'Hatchback'
#     CONVERTIBLE = 'Convertible'
#     CAR_TYPES = [
#         (SEDAN, 'Sedan'),
#         (SUV, 'SUV'),
#         (WAGON, 'Wagon'),
#         (COUPE, 'Coupe'),
#         (HATCHBACK, 'Hatchback'),
#         (CONVERTIBLE, 'Convertible'),
#     ]

#     make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
#     dealer_id = models.IntegerField()  # Refers to dealer in Cloudant DB
#     name = models.CharField(max_length=100)
#     car_type = models.CharField(max_length=20, choices=CAR_TYPES)
#     year = models.DateField()
#     fuel_type = models.CharField(max_length=50, blank=True, null=True)  # Optional field
#     transmission = models.CharField(max_length=50, blank=True, null=True)  # Optional field

#     def __str__(self):
#         return f"{self.make.name} {self.name} ({self.year.year})"

# class CarMake(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField()
#     country = models.CharField(max_length=100, blank=True, null=True)
#     founded_year = models.PositiveIntegerField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.name} - {self.country if self.country else 'N/A'}"


# class CarModel(models.Model):
    # Define choices for car type
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    HATCHBACK = 'Hatchback'
    CONVERTIBLE = 'Convertible'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (HATCHBACK, 'Hatchback'),
        (CONVERTIBLE, 'Convertible'),
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20, choices=CAR_TYPES)
    
    # If you want an integer year field with limits
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])
    
    fuel_type = models.CharField(max_length=50, blank=True, null=True)
    transmission = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year})"