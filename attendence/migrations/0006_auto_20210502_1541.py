# Generated by Django 2.2.17 on 2021-05-02 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0005_auto_20210502_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='branc',
            new_name='branch',
        ),
    ]
