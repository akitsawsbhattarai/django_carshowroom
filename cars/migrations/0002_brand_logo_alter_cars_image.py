# Generated by Django 4.0.1 on 2022-01-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='carimages/'),
        ),
    ]
