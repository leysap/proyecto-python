# Generated by Django 4.1.1 on 2022-11-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_extensionusuario_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extensionusuario',
            name='web',
            field=models.CharField(blank=True, default=0, max_length=50),
            preserve_default=False,
        ),
    ]