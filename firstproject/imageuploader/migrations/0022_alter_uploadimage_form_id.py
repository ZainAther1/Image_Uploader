# Generated by Django 4.0 on 2022-01-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageuploader', '0021_alter_uploadimage_form_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='form_id',
            field=models.CharField(default=1, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
