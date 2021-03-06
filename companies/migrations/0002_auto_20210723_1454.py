# Generated by Django 3.2.5 on 2021-07-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='district',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='postcode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
