# Generated by Django 3.2.9 on 2021-12-06 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
                ('empsalary', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Details',
        ),
    ]
