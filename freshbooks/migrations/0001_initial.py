# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'freshbooks_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('auth_token', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'freshbooks', ['Account'])

        # Adding model 'Client'
        db.create_table(u'freshbooks_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freshbooks.Account'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('work_phone', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('p_street1', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_street2', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_city', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_state', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_country', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_code', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('s_street1', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('s_street2', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('s_city', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('s_state', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('s_country', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('s_code', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('folder', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('recovered', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'freshbooks', ['Client'])

        # Adding model 'Line'
        db.create_table(u'freshbooks_line', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
            ('line_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('unit_cost', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=2)),
            ('tax1_name', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('tax2_name', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('tax1_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=3)),
            ('tax2_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=3)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=2)),
        ))
        db.send_create_signal(u'freshbooks', ['Line'])

        # Adding model 'Invoice'
        db.create_table(u'freshbooks_invoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freshbooks.Account'])),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freshbooks.Client'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('po_number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('terms', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_street1', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_street2', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_city', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_state', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_country', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_code', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=2)),
            ('amount_outstanding', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=2)),
            ('paid', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=2)),
            ('discount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=3)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('folder', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
        ))
        db.send_create_signal(u'freshbooks', ['Invoice'])

        # Adding model 'Estimate'
        db.create_table(u'freshbooks_estimate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freshbooks.Account'])),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['freshbooks.Client'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('po_number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('terms', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_street1', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_street2', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_city', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_state', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_country', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('p_code', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=2)),
            ('discount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=3)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('folder', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
        ))
        db.send_create_signal(u'freshbooks', ['Estimate'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'freshbooks_account')

        # Deleting model 'Client'
        db.delete_table(u'freshbooks_client')

        # Deleting model 'Line'
        db.delete_table(u'freshbooks_line')

        # Deleting model 'Invoice'
        db.delete_table(u'freshbooks_invoice')

        # Deleting model 'Estimate'
        db.delete_table(u'freshbooks_estimate')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'freshbooks.account': {
            'Meta': {'object_name': 'Account'},
            'auth_token': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'freshbooks.client': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Client'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['freshbooks.Account']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_city': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'p_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_state': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_street1': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_street2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'recovered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            's_city': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            's_code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            's_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            's_state': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            's_street1': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            's_street2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'})
        },
        u'freshbooks.estimate': {
            'Meta': {'ordering': "('-number',)", 'object_name': 'Estimate'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['freshbooks.Account']"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['freshbooks.Client']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '3'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_city': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'p_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_state': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_street1': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_street2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'po_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'terms': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'freshbooks.invoice': {
            'Meta': {'ordering': "('-number',)", 'object_name': 'Invoice'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['freshbooks.Account']"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'}),
            'amount_outstanding': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['freshbooks.Client']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '3'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_city': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'p_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_state': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_street1': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'p_street2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'paid': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'}),
            'po_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'terms': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'freshbooks.line': {
            'Meta': {'ordering': "('order', 'line_id', 'id')", 'object_name': 'Line'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'}),
            'tax1_name': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'tax1_percent': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '3'}),
            'tax2_name': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'tax2_percent': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '3'}),
            'unit_cost': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'})
        }
    }

    complete_apps = ['freshbooks']