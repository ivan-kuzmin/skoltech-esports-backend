# Generated by Django 2.1.2 on 2019-02-11 12:59

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('balls', '0004_auto_20190206_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='BallsRedBalls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', jsonfield.fields.JSONField()),
            ],
        ),
    ]
