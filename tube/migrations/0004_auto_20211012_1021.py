# Generated by Django 3.1.7 on 2021-10-12 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0003_showvideos_channel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='showvideos',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='showvideos',
            name='subscribers',
            field=models.IntegerField(default=0),
        ),
    ]