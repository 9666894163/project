# Generated by Django 3.2.9 on 2021-12-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='norman_forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userno', models.IntegerField()),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]
