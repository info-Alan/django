# Generated by Django 4.1.5 on 2023-01-18 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0002_alter_material_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
