# Generated by Django 3.0.3 on 2020-02-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0003_auto_20200226_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='symptom',
            field=models.CharField(default='', max_length=100),
        ),
    ]
