# Generated by Django 2.0.5 on 2018-08-06 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressbook',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
