# Generated by Django 2.0.5 on 2018-06-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('midname', models.CharField(default='', max_length=50)),
                ('surname', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
            ],
        ),
    ]