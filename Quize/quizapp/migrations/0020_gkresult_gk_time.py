# Generated by Django 3.2.3 on 2022-01-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0019_remove_adminu_mesg'),
    ]

    operations = [
        migrations.AddField(
            model_name='gkresult',
            name='gk_time',
            field=models.CharField(default='', max_length=300),
        ),
    ]
