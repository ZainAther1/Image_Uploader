# Generated by Django 4.0 on 2022-01-08 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageuploader', '0011_alter_uploadimage_district_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimage',
            old_name='image_id',
            new_name='form_id',
        ),
    ]
