# Generated by Django 4.1.1 on 2022-11-03 18:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_libro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
