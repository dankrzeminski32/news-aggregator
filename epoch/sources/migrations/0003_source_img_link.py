# Generated by Django 4.2.6 on 2023-11-09 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0002_rename_subsribers_source_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='img_link',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
