from django.contrib import admin

# Register your models here.
from .models import Province, District, Ward, Street

admin.site.register(Province)
admin.site.register(District)
admin.site.register(Ward)
admin.site.register(Street)
