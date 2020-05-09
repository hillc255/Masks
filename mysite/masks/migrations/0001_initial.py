# Generated by Django 3.0.4 on 2020-05-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('materials', models.CharField(blank=True, max_length=800)),
                ('resource', models.URLField(blank=True, max_length=150)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('level', models.CharField(max_length=8, null=True, verbose_name='Level')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('pub_date', models.DateTimeField(null=True, verbose_name='date published')),
            ],
        ),
    ]
