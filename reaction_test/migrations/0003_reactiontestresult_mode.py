# Generated by Django 2.1.2 on 2019-02-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reaction_test', '0002_auto_20190210_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactiontestresult',
            name='mode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
