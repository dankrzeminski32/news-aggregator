# Generated by Django 4.2.6 on 2023-11-07 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='subsribers',
            new_name='subscribers',
        ),
    ]
