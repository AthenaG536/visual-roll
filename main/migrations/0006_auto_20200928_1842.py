# Generated by Django 3.1.1 on 2020-09-28 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200928_1814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['commenttimestamp']},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['date_created']},
        ),
        migrations.AlterModelOptions(
            name='members',
            options={'ordering': ['timestamp']},
        ),
    ]
