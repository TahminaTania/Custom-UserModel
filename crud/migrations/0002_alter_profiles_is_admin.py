# Generated by Django 4.0.1 on 2022-02-23 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
