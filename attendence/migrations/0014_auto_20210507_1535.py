# Generated by Django 2.2.17 on 2021-05-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0013_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='usn',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
