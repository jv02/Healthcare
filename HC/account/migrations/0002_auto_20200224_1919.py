# Generated by Django 2.1.2 on 2020-02-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='bgoup',
            field=models.CharField(choices=[('1', 'O+'), ('2', 'O-'), ('3', 'A+'), ('4', 'A-'), ('5', 'B+'), ('6', 'B-'), ('7', 'AB+'), ('8', 'AB-')], default='O+', max_length=1),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='O+', max_length=1),
        ),
        migrations.AddField(
            model_name='patient',
            name='pincode',
            field=models.IntegerField(default=0),
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
