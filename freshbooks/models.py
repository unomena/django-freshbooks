from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class Account(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    auth_token = models.CharField(max_length=32)

    def __unicode__(self):
        return unicode(self.title)

class Client(models.Model):
    account = models.ForeignKey(Account)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    organization = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField()
    username = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    work_phone = models.CharField(max_length=32, blank=True, null=True)
    home_phone = models.CharField(max_length=32, blank=True, null=True)
    mobile = models.CharField(max_length=32, blank=True, null=True)
    fax = models.CharField(max_length=32, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    p_street1 = models.CharField(max_length=128, blank=True, null=True)
    p_street2 = models.CharField(max_length=128, blank=True, null=True)
    p_city = models.CharField(max_length=128, blank=True, null=True)
    p_state = models.CharField(max_length=128, blank=True, null=True)
    p_country = models.CharField(max_length=128, blank=True, null=True)
    p_code = models.CharField(max_length=16, blank=True, null=True)
    s_street1 = models.CharField(max_length=128, blank=True, null=True)
    s_street2 = models.CharField(max_length=128, blank=True, null=True)
    s_city = models.CharField(max_length=128, blank=True, null=True)
    s_state = models.CharField(max_length=128, blank=True, null=True)
    s_country = models.CharField(max_length=128, blank=True, null=True)
    s_code = models.CharField(max_length=16, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    folder = models.CharField(max_length=16, blank=True, null=True)
    recovered = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return unicode(self.organization)

class Line(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    content_object = generic.GenericForeignKey(content_type, object_id)
    line_id = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    quantity = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    tax1_name = models.CharField(max_length=16, blank=True, null=True)
    tax2_name = models.CharField(max_length=16, blank=True, null=True)
    tax1_percent = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    tax2_percent  = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    amount = models.DecimalField(max_digits=16, decimal_places=2, default=0)

    class Meta:
        ordering = ('order','line_id','id')

class Invoice(models.Model):
    account = models.ForeignKey(Account)
    client = models.ForeignKey(Client)
    number = models.CharField(max_length=32, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    po_number = models.CharField(max_length=32, blank=True, null=True)
    terms = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    organization = models.CharField(max_length=128, blank=True, null=True)
    p_street1 = models.CharField(max_length=128, blank=True, null=True)
    p_street2 = models.CharField(max_length=128, blank=True, null=True)
    p_city = models.CharField(max_length=128, blank=True, null=True)
    p_state = models.CharField(max_length=128, blank=True, null=True)
    p_country = models.CharField(max_length=128, blank=True, null=True)
    p_code = models.CharField(max_length=16, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    amount_outstanding = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    paid = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    status = models.CharField(max_length=16, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    lines = generic.GenericRelation(Line)
    folder = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        ordering = ('-number',)

    def save(self, *args, **kwargs):
        Client.objects.get_or_create(
            id=self.client_id,
            defaults={
                'account':self.account,
                'organization':self.organization,
                'first_name':self.first_name,
                'last_name':self.last_name,
                'p_street1':self.p_street1,
                'p_street2':self.p_street2,
                'p_city':self.p_city,
                'p_state':self.p_state,
                'p_country':self.p_country,
                'p_code':self.p_code,
                'recovered':True
            }
        )
        super(Invoice, self).save(*args, **kwargs)

class Estimate(models.Model):
    account = models.ForeignKey(Account)
    client = models.ForeignKey(Client)
    number = models.CharField(max_length=32, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    po_number = models.CharField(max_length=32, blank=True, null=True)
    terms = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    organization = models.CharField(max_length=128, blank=True, null=True)
    p_street1 = models.CharField(max_length=128, blank=True, null=True)
    p_street2 = models.CharField(max_length=128, blank=True, null=True)
    p_city = models.CharField(max_length=128, blank=True, null=True)
    p_state = models.CharField(max_length=128, blank=True, null=True)
    p_country = models.CharField(max_length=128, blank=True, null=True)
    p_code = models.CharField(max_length=16, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    status = models.CharField(max_length=16, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    lines = generic.GenericRelation(Line)
    folder = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        ordering = ('-number',)

    def save(self, *args, **kwargs):
        Client.objects.get_or_create(
            id=self.client_id,
            defaults={
                'account':self.account,
                'organization':self.organization,
                'first_name':self.first_name,
                'last_name':self.last_name,
                'p_street1':self.p_street1,
                'p_street2':self.p_street2,
                'p_city':self.p_city,
                'p_state':self.p_state,
                'p_country':self.p_country,
                'p_code':self.p_code,
                'recovered':True
            }
        )
        super(Estimate, self).save(*args, **kwargs)
