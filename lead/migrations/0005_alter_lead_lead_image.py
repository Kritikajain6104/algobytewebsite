# Generated by Django 4.1.2 on 2023-01-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0004_alter_lead_lead_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='lead_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to=''),
        ),
    ]
