# Generated by Django 5.0 on 2023-12-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Name')),
                ('gender', models.CharField(blank=True, max_length=1, verbose_name='Gender')),
                ('birthday', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User',
            },
        ),
    ]
