from django.contrib import admin
# from .models import related models

from django.contrib import admin
from .models import CarMake, CarModel

# Register models so they show up in the admin site
admin.site.register(CarMake)
admin.site.register(CarModel)

# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
