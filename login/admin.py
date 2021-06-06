from django.contrib import admin
from .models import anntbl, Author, Roles

admin.site.register(anntbl)
admin.site.register(Author)
admin.site.register(Roles)