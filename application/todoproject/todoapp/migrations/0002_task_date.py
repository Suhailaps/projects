# Generated by Django 4.2.5 on 2023-10-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2003-01-22'),
            preserve_default=False,
        ),
    ]
