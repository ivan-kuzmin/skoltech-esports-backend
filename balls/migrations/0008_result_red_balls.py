# Generated by Django 2.1.2 on 2019-02-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balls', '0007_auto_20190217_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='red_balls',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]