# encoding: utf8
from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('user', models.OneToOneField(to_field='id', to=settings.AUTH_USER_MODEL)),
                ('birthday', models.DateField(verbose_name=datetime.date(1994, 4, 25))),
                ('home', models.CharField(max_length=200, default='Hanoi')),
                ('score_of_the_last_test', models.IntegerField(default=0)),
                ('total_score', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
