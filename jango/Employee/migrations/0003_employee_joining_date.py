# Generated by Django 3.2.9 on 2021-12-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_auto_20211206_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='joining_date',
            field=models.DateField(null=True),
        ),
    ]
