from django.core.management.base import BaseCommand

from freshbooks import api, models

class Command(BaseCommand):

    def handle(self, *args, **options):

        for acc in models.Account.objects.all():

            api.setup(acc)

#            for o in api.Client.list(get_all=True):
#                o.sync(models.Client)

#            for o in api.Invoice.list(get_all=True):
#                o.sync(models.Invoice, models.Line)

            for o in api.Estimate.list(get_all=True):
                o.sync(models.Estimate, models.Line)
