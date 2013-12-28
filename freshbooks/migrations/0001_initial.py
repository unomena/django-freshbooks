# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'freshbooks_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('freshbooks_id', self.gf('django.db.models.fields.IntegerField')()),
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
            ('s_country', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('s_code', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'freshbooks', ['Client'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'freshbooks_client')


    models = {
        u'freshbooks.client': {
            'Meta': {'object_name': 'Client'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'freshbooks_id': ('django.db.models.fields.IntegerField', [], {}),
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
            's_city': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            's_code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            's_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            's_street1': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            's_street2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['freshbooks']