# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Like'
        db.create_table(u'like_like', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_type', self.gf('django.db.models.fields.IntegerField')()),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('ts', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 8, 30, 0, 0))),
        ))
        db.send_create_signal(u'like', ['Like'])


    def backwards(self, orm):
        # Deleting model 'Like'
        db.delete_table(u'like_like')


    models = {
        u'like.like': {
            'Meta': {'object_name': 'Like'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'object_type': ('django.db.models.fields.IntegerField', [], {}),
            'ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 8, 30, 0, 0)'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['like']