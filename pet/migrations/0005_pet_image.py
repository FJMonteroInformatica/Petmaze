# Generated by Django 4.2.7 on 2023-12-01 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_alter_pet_breed'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(null=True, upload_to='static/sstatic/images'),
        ),
    ]
