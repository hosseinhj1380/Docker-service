# Generated by Django 4.2.6 on 2023-10-11 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run_docker_app', '0003_logs_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date writed '),
        ),
    ]