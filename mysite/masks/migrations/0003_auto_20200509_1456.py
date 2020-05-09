# Generated by Django 3.0.4 on 2020-05-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masks', '0002_auto_20200509_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='level',
            field=models.CharField(choices=[('EASY', 'Easy'), ('SOSO', 'So-so'), ('HARD', 'Hard')], default='EASY', max_length=6),
        ),
    ]