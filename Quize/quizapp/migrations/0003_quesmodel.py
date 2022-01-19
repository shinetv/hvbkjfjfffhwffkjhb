# Generated by Django 3.2.3 on 2021-12-26 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_adminu_std_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('user_IDD', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizapp.adminu')),
            ],
        ),
    ]