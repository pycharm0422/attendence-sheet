# Generated by Django 2.2.17 on 2021-05-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0007_auto_20210502_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='branch',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='your_favorite_quote',
            field=models.TextField(blank=True, null=True),
        ),
    ]
