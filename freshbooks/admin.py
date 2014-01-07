from django.contrib import admin
from django.contrib.contenttypes import generic
from freshbooks import models

class ClientAdmin(admin.ModelAdmin):
    list_display = ('account', 'id', 'organization', 'first_name', 'last_name')
    list_display_links = ('organization',)

class LineInline(generic.GenericTabularInline):
    model = models.Line

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [LineInline]
    list_display = ('account', 'client', 'number', 'date', 'amount', 'paid', 'status', 'folder')
    list_display_links = ('number',)
    list_filter = ('client',)

class EstimateAdmin(admin.ModelAdmin):
    inlines = [LineInline]
    list_display = ('account', 'client', 'number', 'date', 'amount', 'status', 'folder')
    list_display_links = ('number',)
    list_filter = ('client',)

admin.site.register(models.Account)
admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.Estimate, EstimateAdmin)
