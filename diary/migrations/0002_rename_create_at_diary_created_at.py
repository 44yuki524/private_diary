# Generated by Django 3.2.7 on 2024-08-13 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
