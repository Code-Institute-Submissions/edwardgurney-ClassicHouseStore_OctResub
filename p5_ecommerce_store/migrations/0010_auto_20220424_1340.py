# Generated by Django 3.2 on 2022-04-24 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p5_ecommerce_store', '0009_alter_rating_rating_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='audio_file',
            new_name='preview_audio_file',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='audio_link',
            new_name='preview_audio_link',
        ),
    ]
