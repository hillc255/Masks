# Generated by Django 3.0.4 on 2020-05-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masks', '0016_auto_20200508_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='show_url',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
