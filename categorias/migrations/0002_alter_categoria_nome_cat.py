# Generated by Django 4.1.2 on 2022-10-20 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome_cat',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
    ]
