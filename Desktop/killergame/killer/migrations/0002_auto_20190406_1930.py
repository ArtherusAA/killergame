# Generated by Django 2.2 on 2019-04-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('killer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=21),
        ),
    ]
