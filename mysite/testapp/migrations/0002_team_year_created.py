# Generated by Django 4.1 on 2023-10-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='year_created',
            field=models.IntegerField(null=True),
        ),
    ]
