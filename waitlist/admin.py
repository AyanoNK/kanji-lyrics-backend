from django.contrib import admin
from .models import Waitlist


# Custom classes
class GatewayPaymentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Waitlist._meta.fields]


admin.site.register(Waitlist, GatewayPaymentAdmin)
