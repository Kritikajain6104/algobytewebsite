# Generated by Django 4.1.2 on 2023-01-28 13:49

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=20)),
                ('blog_shortdecs', models.CharField(max_length=100)),
                ('blog_desc', tinymce.models.HTMLField()),
            ],
        ),
    ]
