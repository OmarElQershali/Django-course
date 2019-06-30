from django.contrib import admin
from .models import Publisher , Author , Book
# Register your models here.
admin.site.register(Publisher , Author , Book)