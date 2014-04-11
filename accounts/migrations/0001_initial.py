# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user', models.OneToOneField(to_field='id', to=settings.AUTH_USER_MODEL)),
                ('website', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
