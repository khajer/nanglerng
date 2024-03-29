# Generated by Django 4.0.2 on 2022-04-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanglerng', '0012_alter_post_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contribute',
            new_name='contributor',
        ),
        migrations.AlterField(
            model_name='post',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
    ]
