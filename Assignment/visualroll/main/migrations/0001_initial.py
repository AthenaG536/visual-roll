# Generated by Django 3.1.1 on 2020-09-19 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(verbose_name='Email')),
                ('first_name', models.TextField(verbose_name='First Name')),
                ('last_name', models.TextField(verbose_name='Last Name')),
                ('password', models.TextField(verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.TextField(verbose_name='Group Name')),
                ('g_info', models.TextField(verbose_name='Group Info')),
                ('date_created', models.DateField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.user')),
            ],
        ),
    ]
