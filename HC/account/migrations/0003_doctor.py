# Generated by Django 2.1.2 on 2020-02-24 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200224_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('firstname', models.CharField(default='', max_length=100)),
                ('lastname', models.CharField(default='', max_length=100)),
                ('aadharno', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('phoneno', models.IntegerField(default=0)),
                ('contactno', models.IntegerField(default=0)),
                ('pincode', models.IntegerField(default=0)),
                ('degree', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='123', max_length=100)),
                ('confirmpassword', models.CharField(default='123', max_length=100)),
            ],
        ),
    ]
