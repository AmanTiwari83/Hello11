# Generated by Django 3.2.4 on 2023-11-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100, null=True)),
                ('des', models.TextField(null=True)),
            ],
        ),
    ]
