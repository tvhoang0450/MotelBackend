from django.contrib import admin

# Register your models here.
from .models import District
from .models import Ward
admin.site.register(District)
admin.site.register(Ward)