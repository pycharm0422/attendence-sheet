# Generated by Django 2.2.17 on 2021-05-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0009_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_present',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
