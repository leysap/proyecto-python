# Generated by Django 4.1.1 on 2022-10-16 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]