# Generated by Django 4.0 on 2022-02-04 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_application_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='design_doc',
            field=models.FileField(blank=True, null=True, upload_to='design_doc'),
        ),
    ]