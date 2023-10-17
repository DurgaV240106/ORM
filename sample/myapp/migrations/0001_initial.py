# Generated by Django 4.2.5 on 2023-10-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=20)),
                ('team_name', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('DOB', models.DateField()),
            ],
        ),
    ]
