# Generated by Django 2.2.12 on 2020-07-06 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0023_auto_20200706_0627'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GWStringType',
            new_name='SpringType',
        ),
        migrations.AlterField(
            model_name='gwwell',
            name='gw_well_yield',
            field=models.ForeignKey(blank=True, help_text='Estimated or calculated yield from a well.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.GWYield', verbose_name='gwWellYield'),
        ),
    ]
