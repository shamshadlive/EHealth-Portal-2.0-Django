# Generated by Django 4.1.1 on 2022-10-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_bookingpatient_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
