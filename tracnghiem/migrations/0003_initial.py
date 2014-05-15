# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'tracnghiem_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'tracnghiem', ['Question'])

        # Adding model 'Choice'
        db.create_table(u'tracnghiem_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracnghiem.Question'])),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('is_correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.CharField')(default=0, max_length=4)),
        ))
        db.send_create_signal(u'tracnghiem', ['Choice'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'tracnghiem_question')

        # Deleting model 'Choice'
        db.delete_table(u'tracnghiem_choice')


    models = {
        u'tracnghiem.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '4'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracnghiem.Question']"})
        },
        u'tracnghiem.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['tracnghiem']