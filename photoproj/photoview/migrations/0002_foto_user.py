# Generated by Django 3.2.12 on 2023-12-13 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photoview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photoview_user.user'),
            preserve_default=False,
        ),
    ]