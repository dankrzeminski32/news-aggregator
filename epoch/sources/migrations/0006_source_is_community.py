# Generated by Django 4.2.6 on 2023-11-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0005_alter_headline_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='is_community',
            field=models.BooleanField(default=False),
        ),
    ]