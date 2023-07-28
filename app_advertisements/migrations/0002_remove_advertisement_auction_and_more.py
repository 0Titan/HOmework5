# Generated by Django 4.2.3 on 2023-07-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='created_dt',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='description',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='updated_dt',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
