# Generated by Django 2.2.12 on 2020-07-08 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0025_auto_20200706_0721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gwwell',
            old_name='gwWellReferenceElevation',
            new_name='gw_well_reference_elevation',
        ),
    ]
