# Generated by Django 2.2.12 on 2020-07-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0002_auto_20200702_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachmentmethodterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bodyqualitytype',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casingcoatingterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casingformterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casingmaterialterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='filtrationmaterialterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='omprocess',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perforationmethodterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='unit',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screencoatingterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screenfittingterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screenformterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screenmakerterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screenmaterialterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screenmodelterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screennumberterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screenplacementterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sealingmaterialterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sealingtypeterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vulnerabilitytype',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wellstatustypeterm',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
