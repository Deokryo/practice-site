# Generated by Django 3.2.13 on 2022-07-02 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
