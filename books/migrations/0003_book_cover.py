# Generated by Django 2.2.7 on 2019-12-27 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='cover/default.png', upload_to='cover/'),
        ),
    ]
