# Generated by Django 2.2.12 on 2020-07-06 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0021_auto_20200706_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='gwwaterbudget',
            name='gw_budget_valid_time',
            field=models.ForeignKey(blank=True, help_text='Valid time of this budget (e.g., 2010).', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TemporalType', verbose_name='GWBudgetValidTime'),
        ),
    ]
