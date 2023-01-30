from django.contrib import admin
from .models import *

admin.site.register(bank)
admin.site.register(supplier)
admin.site.register(customer)
admin.site.register([request_invoice,approve_invoice,deny_invoice,view_invoice,upload_invoice])

# Register your models here.
