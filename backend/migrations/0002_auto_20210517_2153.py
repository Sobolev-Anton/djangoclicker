# Generated by Django 3.2 on 2021-05-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maincycle',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
