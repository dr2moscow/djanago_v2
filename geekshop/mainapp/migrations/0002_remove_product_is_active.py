# Generated by Django 3.2.5 on 2021-08-11 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_active',
        ),
    ]
