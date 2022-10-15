# Generated by Django 4.1.1 on 2022-10-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
                ('categoria', models.IntegerField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_creacion', models.DateTimeField()),
            ],
        ),
    ]
