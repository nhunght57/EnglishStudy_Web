# encoding: utf8
from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default='22/8/1994'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Score_of_the_last_test',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(verbose_name='password', max_length=128, default='admin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='home',
            field=models.CharField(max_length=200, default='ha noi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Total_score',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
