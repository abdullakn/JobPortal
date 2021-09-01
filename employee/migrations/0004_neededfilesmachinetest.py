# Generated by Django 3.2.5 on 2021-08-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_remove_skillbadges_scores'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeededFilesMachineTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machinetest', models.CharField(blank=True, max_length=200, null=True)),
                ('github', models.CharField(blank=True, max_length=200, null=True)),
                ('compressed', models.FileField(blank=True, null=True, upload_to='machine_test')),
                ('host', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]