# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Registrant'
        db.create_table(u'landing_page_registrant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=63)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
        ))
        db.send_create_signal(u'landing_page', ['Registrant'])

        # Adding model 'Photo'
        db.create_table(u'landing_page_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image_path', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('inPool', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user_link', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'landing_page', ['Photo'])

        # Adding model 'Tag'
        db.create_table(u'landing_page_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['landing_page.Photo'])),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
            ('angle', self.gf('django.db.models.fields.IntegerField')()),
            ('colour', self.gf('django.db.models.fields.CharField')(default='black', max_length=10, blank=True)),
        ))
        db.send_create_signal(u'landing_page', ['Tag'])

        # Adding model 'Meta'
        db.create_table(u'landing_page_meta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num_users', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'landing_page', ['Meta'])


    def backwards(self, orm):
        # Deleting model 'Registrant'
        db.delete_table(u'landing_page_registrant')

        # Deleting model 'Photo'
        db.delete_table(u'landing_page_photo')

        # Deleting model 'Tag'
        db.delete_table(u'landing_page_tag')

        # Deleting model 'Meta'
        db.delete_table(u'landing_page_meta')


    models = {
        u'landing_page.meta': {
            'Meta': {'object_name': 'Meta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_users': ('django.db.models.fields.IntegerField', [], {})
        },
        u'landing_page.photo': {
            'Meta': {'object_name': 'Photo'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'inPool': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'landing_page.registrant': {
            'Meta': {'object_name': 'Registrant'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '63'})
        },
        u'landing_page.tag': {
            'Meta': {'object_name': 'Tag'},
            'angle': ('django.db.models.fields.IntegerField', [], {}),
            'colour': ('django.db.models.fields.CharField', [], {'default': "'black'", 'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['landing_page.Photo']"}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['landing_page']