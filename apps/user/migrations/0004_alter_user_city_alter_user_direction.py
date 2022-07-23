# Generated by Django 4.0.6 on 2022-07-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direction', '0002_alter_direction_parent'),
        ('user', '0003_remove_developer_direction_remove_developer_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mесто жительства'),
        ),
        migrations.AlterField(
            model_name='user',
            name='direction',
            field=models.ManyToManyField(blank=True, null=True, to='direction.direction', verbose_name='Направления'),
        ),
    ]
