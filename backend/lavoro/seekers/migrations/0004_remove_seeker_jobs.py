# Generated by Django 2.0.3 on 2018-03-09 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seekers', '0003_auto_20180309_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seeker',
            name='jobs',
        ),
    ]
