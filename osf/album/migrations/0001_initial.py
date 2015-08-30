# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table(u'album_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('album_id', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('ts', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 8, 30, 0, 0))),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'album', ['Photo'])

        # Adding model 'Album'
        db.create_table(u'album_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('create_ts', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 8, 30, 0, 0))),
            ('album_title', self.gf('django.db.models.fields.CharField')(default='New Album', max_length=100)),
            ('album_desc', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('last_add_ts', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('photos_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cover', self.gf('django.db.models.fields.URLField')(default='http://7xjfbe.com1.z0.glb.clouddn.com/23.jpg', max_length=200)),
            ('like_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('share_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comment_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'album', ['Album'])

        # Adding M2M table for field photos on 'Album'
        m2m_table_name = db.shorten_name(u'album_album_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm[u'album.album'], null=False)),
            ('photo', models.ForeignKey(orm[u'album.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['album_id', 'photo_id'])

        # Adding M2M table for field tags on 'Album'
        m2m_table_name = db.shorten_name(u'album_album_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm[u'album.album'], null=False)),
            ('tag', models.ForeignKey(orm[u'tag.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['album_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table(u'album_photo')

        # Deleting model 'Album'
        db.delete_table(u'album_album')

        # Removing M2M table for field photos on 'Album'
        db.delete_table(db.shorten_name(u'album_album_photos'))

        # Removing M2M table for field tags on 'Album'
        db.delete_table(db.shorten_name(u'album_album_tags'))


    models = {
        u'album.album': {
            'Meta': {'object_name': 'Album'},
            'album_desc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'album_title': ('django.db.models.fields.CharField', [], {'default': "'New Album'", 'max_length': '100'}),
            'comment_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cover': ('django.db.models.fields.URLField', [], {'default': "'http://7xjfbe.com1.z0.glb.clouddn.com/23.jpg'", 'max_length': '200'}),
            'create_ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 8, 30, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_add_ts': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'like_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['album.Photo']", 'symmetrical': 'False'}),
            'photos_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'share_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tag.Tag']", 'symmetrical': 'False'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'album.photo': {
            'Meta': {'object_name': 'Photo'},
            'album_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 8, 30, 0, 0)'})
        },
        u'tag.tag': {
            'Meta': {'object_name': 'Tag'},
            'add_ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 8, 30, 0, 0)'}),
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['album']