# Generated by Django 2.0.3 on 2018-03-09 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seekers', '0004_remove_seeker_jobs'),
        ('jobs', '0002_auto_20180309_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='seeker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='seekers.Seeker'),
            preserve_default=False,
        ),
    ]
