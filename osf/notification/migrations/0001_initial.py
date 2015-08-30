# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Notification'
        db.create_table(u'notification_notification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('notify_type', self.gf('django.db.models.fields.IntegerField')()),
            ('notify_id', self.gf('django.db.models.fields.IntegerField')()),
            ('object_type', self.gf('django.db.models.fields.IntegerField')()),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
            ('notified_user', self.gf('django.db.models.fields.IntegerField')()),
            ('notifier', self.gf('django.db.models.fields.IntegerField')()),
            ('ts', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 8, 30, 0, 0))),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('notifier_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('notifier_avatar', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('object_title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'notification', ['Notification'])


    def backwards(self, orm):
        # Deleting model 'Notification'
        db.delete_table(u'notification_notification')


    models = {
        u'notification.notification': {
            'Meta': {'object_name': 'Notification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notified_user': ('django.db.models.fields.IntegerField', [], {}),
            'notifier': ('django.db.models.fields.IntegerField', [], {}),
            'notifier_avatar': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'notifier_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'notify_id': ('django.db.models.fields.IntegerField', [], {}),
            'notify_type': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'object_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'object_type': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 8, 30, 0, 0)'})
        }
    }

    complete_apps = ['notification']