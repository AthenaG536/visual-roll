# Generated by Django 3.1.1 on 2020-09-18 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.TextField(verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.TextField(verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(verbose_name='Password'),
        ),
    ]