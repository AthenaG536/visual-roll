# Generated by Django 3.1.1 on 2020-10-03 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20201002_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(default=2465862543008, on_delete=django.db.models.deletion.CASCADE, to='main.group'),
        ),
    ]
