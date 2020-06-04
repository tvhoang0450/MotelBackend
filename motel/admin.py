from django.contrib import admin

# Register your models here.
from .models import TypeMotel, baseInforMotel, Service, Board, ImageMotel

admin.site.register(TypeMotel)
admin.site.register(baseInforMotel)
admin.site.register(Service)
admin.site.register(Board)
admin.site.register(ImageMotel)
