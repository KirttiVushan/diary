# Generated by Django 3.0.3 on 2020-10-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0002_auto_20200923_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='dateaccessed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
