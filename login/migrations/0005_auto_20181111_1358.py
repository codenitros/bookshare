# Generated by Django 2.1 on 2018-11-11 08:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20181105_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='USN',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9A-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sem',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year',
            field=models.IntegerField(),
        ),
    ]
