# Generated by Django 2.0.3 on 2018-03-17 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180317_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default='20', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, default='20', editable=False, null=True),
        ),
    ]