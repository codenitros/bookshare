# Generated by Django 2.1 on 2018-11-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
