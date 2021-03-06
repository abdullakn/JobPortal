# Generated by Django 3.2.5 on 2021-07-30 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=200, null=True)),
                ('option1', models.CharField(blank=True, max_length=200, null=True)),
                ('option2', models.CharField(blank=True, max_length=200, null=True)),
                ('option3', models.CharField(blank=True, max_length=200, null=True)),
                ('option4', models.CharField(blank=True, max_length=200, null=True)),
                ('answer', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.categorydomain')),
            ],
        ),
    ]
