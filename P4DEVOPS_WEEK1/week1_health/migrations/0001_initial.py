# Generated by Django 5.2 on 2025-04-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemHealth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cpu_usage', models.FloatField()),
                ('memory_usage', models.FloatField()),
                ('disk_usage', models.FloatField()),
            ],
        ),
    ]
