# Generated by Django 2.2.17 on 2021-05-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0016_auto_20210508_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
