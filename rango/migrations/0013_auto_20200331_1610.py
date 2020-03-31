# Generated by Django 2.2.3 on 2020-03-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0012_auto_20200330_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(choices=[('Pop', 'POP'), ('Rock', 'ROCK'), ('Metal', 'METAL'), ('Soul', 'SOUL'), ('Electronic', 'ELECTRONIC'), ('R&B', 'R&B'), ('Hip-Hop', 'HIP-HOP'), ('Indie', 'INDIE'), ('Classical', 'CLASSICAL'), ('Country', 'COUNTRY'), ('Jazz', 'JAZZ')], default='Pop', max_length=15),
        ),
    ]
