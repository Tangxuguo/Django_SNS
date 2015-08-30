# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'event_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ts', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 8, 30, 0, 0))),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('user_avatar', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('like_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('share_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comment_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=10000, blank=True)),
            ('following_user_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('following_user_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('follower_user_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('follower_user_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('is_like', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'event', ['Event'])

        # Adding M2M table for field photos on 'Event'
        m2m_table_name = db.shorten_name(u'event_event_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'event.event'], null=False)),
            ('photo', models.ForeignKey(orm[u'album.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'photo_id'])

        # Adding M2M table for field tags on 'Event'
        m2m_table_name = db.shorten_name(u'event_event_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'event.event'], null=False)),
            ('tag', models.ForeignKey(orm[u'tag.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'event_event')

        # Removing M2M table for field photos on 'Event'
        db.delete_table(db.shorten_name(u'event_event_photos'))

        # Removing M2M table for field tags on 'Event'
        db.delete_table(db.shorten_name(u'event_event_tags'))


    models = {
        u'album.photo': {
            'Meta': {'object_name': 'Photo'},
            'album_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 8, 30, 0, 0)'})
        },
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'comment_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'blank': 'True'}),
            'follower_user_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'follower_user_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'following_user_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'following_user_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_like': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'like_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'object_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['album.Photo']", 'symmetrical': 'False'}),
            'share_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tag.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 8, 30, 0, 0)'}),
            'user_avatar': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'tag.tag': {
            'Meta': {'object_name': 'Tag'},
            'add_ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 8, 30, 0, 0)'}),
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['event']