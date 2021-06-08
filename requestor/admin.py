from django.contrib import admin
from .models import (Requestor, Category, SubCategory,
                    SupportCategory, Sector,
                    SectorForScholarship,
                    Status,
                    RequestorLog)

# Register your models here.
admin.site.register(Requestor)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SupportCategory)
admin.site.register(Sector)
admin.site.register(SectorForScholarship)
admin.site.register(Status)
admin.site.register(RequestorLog)
