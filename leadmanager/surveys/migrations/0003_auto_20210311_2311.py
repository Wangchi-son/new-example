# Generated by Django 3.1.7 on 2021-03-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_auto_20210311_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='Rest',
            field=models.SlugField(allow_unicode=True, choices=[('inbusiness', 'Inbusiness'), ('outbusiness', 'Outbusiness'), ('home', 'Home'), ('intravle', 'Intravle'), ('outtravle', 'Outtravle')], max_length=100, null=True, unique=True),
        ),
    ]