# Generated by Django 2.2.6 on 2020-01-08 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20200108_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='submitter',
            field=models.CharField(default='', max_length=200),
        ),
    ]
