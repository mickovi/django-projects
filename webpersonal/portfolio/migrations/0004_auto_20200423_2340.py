# Generated by Django 2.2 on 2020-04-23 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200423_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección web'),
        ),
    ]
