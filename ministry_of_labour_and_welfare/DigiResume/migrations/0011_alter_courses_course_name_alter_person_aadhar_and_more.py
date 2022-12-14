# Generated by Django 4.1 on 2022-08-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigiResume', '0010_alter_educationinfo_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='aadhar',
            field=models.IntegerField(max_length=16),
        ),
        migrations.AlterField(
            model_name='rolesbyinstitution',
            name='role_name',
            field=models.CharField(max_length=100),
        ),
    ]
