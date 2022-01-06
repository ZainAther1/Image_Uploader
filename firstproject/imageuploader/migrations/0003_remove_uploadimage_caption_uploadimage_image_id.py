# Generated by Django 4.0 on 2022-01-05 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageuploader', '0002_alter_uploadimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadimage',
            name='caption',
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='image_id',
            field=models.CharField(default=1, max_length=200, unique=True),
        ),
    ]
