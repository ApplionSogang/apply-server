# Generated by Django 4.0 on 2022-02-02 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer1', models.TextField(blank=True, default='')),
                ('answer2', models.TextField(blank=True, default='')),
                ('answer3', models.TextField(blank=True, default='')),
                ('answer4', models.TextField(blank=True, default='')),
                ('answer5', models.TextField(blank=True, default='')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('portfolio', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
