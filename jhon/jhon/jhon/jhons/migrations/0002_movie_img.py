# Generated by Django 4.2.1 on 2023-08-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jhons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ddffdfs', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
