# Generated by Django 3.2.3 on 2021-12-31 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0016_auto_20211230_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='ap_date',
            field=models.CharField(default='', max_length=100),
        ),
    ]
