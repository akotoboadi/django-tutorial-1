# Generated by Django 5.0.6 on 2024-11-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_team_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='age',
        ),
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
