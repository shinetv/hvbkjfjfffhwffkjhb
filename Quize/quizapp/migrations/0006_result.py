# Generated by Django 3.2.3 on 2021-12-29 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0005_aptitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(default='', max_length=1000)),
                ('percentage', models.CharField(default='', max_length=1000)),
                ('User_iDD', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizapp.adminu')),
            ],
        ),
    ]
