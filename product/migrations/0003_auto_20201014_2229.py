# Generated by Django 3.1.2 on 2020-10-15 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201014_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='preco',
        ),
    ]
