# Generated by Django 4.2.2 on 2024-05-07 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0037_nursedetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nursedetail',
            name='doctorId',
        ),
        migrations.RemoveField(
            model_name='nursedetail',
            name='doctorName',
        ),
        migrations.RemoveField(
            model_name='nursedetail',
            name='patientId',
        ),
        migrations.RemoveField(
            model_name='nursedetail',
            name='patientName',
        ),
    ]
