# Generated by Django 3.0.3 on 2020-02-25 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disname', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('aadhard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docpatient', to='account.Doctor')),
                ('aadharp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patientaadhar', to='account.Patient')),
                ('disid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disease', to='disease.Disease')),
            ],
        ),
    ]
