# Generated by Django 4.0.6 on 2022-07-23 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='direction.direction'),
        ),
    ]
