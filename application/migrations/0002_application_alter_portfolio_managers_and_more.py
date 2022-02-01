# Generated by Django 4.0 on 2022-02-01 03:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_is_staff_customuser_is_superuser'),
        ('application', '0001_initial'),
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
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
            ],
        ),
        migrations.AlterModelManagers(
            name='portfolio',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='user_id',
            new_name='user',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]