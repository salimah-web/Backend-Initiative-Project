# Generated by Django 3.1.5 on 2021-01-12 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='producer',
            field=models.CharField(max_length=30),
        ),
    ]