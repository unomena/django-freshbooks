from django.core.management.base import BaseCommand
from django.conf import settings

from freshbooks import api, models

class Command(BaseCommand):

    def sync_clients(self):
        objects = api.Client.list(get_all=True)
        model = models.Client
        for o in objects:
           o.sync(model)
    
    def sync_invoices(self):
        objects = api.Invoice.list(get_all=True)
        model = models.Invoice
        for o in objects:
            o.sync(model)

    def handle(self, *args, **options):
        
        api.setup(
            '%s.freshbooks.com' % settings.FRESHBOOKS_APP_NAME,
            settings.FRESHBOOKS_AUTH_TOKEN,
            settings.FRESHBOOKS_APP_NAME
        )

        self.sync_clients()
        self.sync_invoices()
