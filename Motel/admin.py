from django.contrib import admin

# Register your models here.
from .models import Motel
from .models import MotelTypes

admin.site.register(Motel)
admin.site.register(MotelTypes)