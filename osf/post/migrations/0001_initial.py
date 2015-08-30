# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'post_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.IntegerField')()),
            ('ts', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 8, 30, 0, 0))),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(default='New Post', max_length=100)),
            ('excerpt', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comment_status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pwd', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('lastts', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('like_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('share_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comment_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('album', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cover', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'post', ['Post'])

        # Adding M2M table for field tags on 'Post'
        m2m_table_name = db.shorten_name(u'post_post_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'post.post'], null=False)),
            ('tag', models.ForeignKey(orm[u'tag.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'post_post')

        # Removing M2M table for field tags on 'Post'
        db.delete_table(db.shorten_name(u'post_post_tags'))


    models = {
        u'post.post': {
            'Meta': {'object_name': 'Post'},
            'album': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'author': ('django.db.models.fields.IntegerField', [], {}),
            'comment_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'comment_status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastts': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'like_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pwd': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'share_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tag.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'New Post'", 'max_length': '100'}),
            'ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 8, 30, 0, 0)'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'tag.tag': {
            'Meta': {'object_name': 'Tag'},
            'add_ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 8, 30, 0, 0)'}),
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['post']