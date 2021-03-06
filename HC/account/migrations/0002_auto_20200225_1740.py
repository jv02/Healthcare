# Generated by Django 3.0.3 on 2020-02-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disid', models.AutoField(primary_key=True, serialize=False)),
                ('disname', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='xyz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='aadhar_no',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='conf_password',
            field=models.CharField(default='123', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='password',
            field=models.CharField(default='123', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_no',
            field=models.IntegerField(default=0),
        ),
    ]
