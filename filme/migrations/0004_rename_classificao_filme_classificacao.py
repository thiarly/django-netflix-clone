# Generated by Django 4.2.2 on 2023-06-13 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0003_remove_filme_numero_views_filme_classificao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filme',
            old_name='classificao',
            new_name='classificacao',
        ),
    ]