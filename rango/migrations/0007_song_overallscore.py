# Generated by Django 2.2.3 on 2020-03-23 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20200322_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='overallScore',
            field=models.IntegerField(default=0),
        ),
    ]
