# Generated by Django 3.2.12 on 2024-06-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoview', '0002_foto_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='main_color',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
    ]