# Generated by Django 2.2.17 on 2021-07-17 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0038_studentmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendence.Student'),
        ),
    ]