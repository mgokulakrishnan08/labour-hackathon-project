# Generated by Django 4.0.6 on 2022-08-09 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DigiResume', '0008_alter_person_district_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='workinfobyinstitution',
            unique_together={('uid', 'inst_code', 'role')},
        ),
        migrations.AlterUniqueTogether(
            name='workinfobyorganisation',
            unique_together={('uid', 'org_code', 'role')},
        ),
    ]
