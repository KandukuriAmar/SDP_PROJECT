# Generated by Django 4.2.5 on 2024-02-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('Comment', models.CharField(max_length=100000)),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
    ]
