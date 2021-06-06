from django.contrib import admin
from .models import TravelRequest_tbl, History_tbl, request_category, travel_sector, travel_office, Pending_training_report, Pending_remarks

# Register your models here.
admin.site.register(TravelRequest_tbl)
admin.site.register(History_tbl)
admin.site.register(request_category)
admin.site.register(travel_sector)
admin.site.register(travel_office)
admin.site.register(Pending_training_report)
admin.site.register(Pending_remarks)

