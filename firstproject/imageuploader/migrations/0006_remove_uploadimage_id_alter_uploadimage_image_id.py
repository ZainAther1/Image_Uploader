# Generated by Django 4.0 on 2022-01-05 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageuploader', '0005_alter_uploadimage_desc_alter_uploadimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadimage',
            name='id',
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='image_id',
            field=models.CharField(default=1, max_length=20, primary_key=True, serialize=False),
        ),
    ]