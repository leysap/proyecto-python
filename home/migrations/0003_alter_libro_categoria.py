# Generated by Django 4.1.1 on 2022-10-15 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_libro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.IntegerField(),
        ),
    ]
