# Generated by Django 4.1.1 on 2022-11-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extensionusuario',
            name='web',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]