# Generated by Django 4.0.1 on 2022-02-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_brand_logo_alter_cars_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]