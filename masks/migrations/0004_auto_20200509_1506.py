# Generated by Django 3.0.4 on 2020-05-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masks', '0003_auto_20200509_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='level',
            field=models.CharField(choices=[('Easy', 'Easy'), ('So-so', 'So-so'), ('Hard', 'Hard')], default='Easy', max_length=6),
        ),
    ]