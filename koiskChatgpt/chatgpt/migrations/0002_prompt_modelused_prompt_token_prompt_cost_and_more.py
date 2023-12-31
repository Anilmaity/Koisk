# Generated by Django 4.2.2 on 2023-06-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='Modelused',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='prompt',
            name='Token',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='prompt',
            name='cost',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='prompt',
            name='Promt_message',
            field=models.TextField(blank=True, max_length=1600000),
        ),
        migrations.AlterField(
            model_name='prompt',
            name='Response',
            field=models.TextField(blank=True, max_length=1600000),
        ),
    ]
