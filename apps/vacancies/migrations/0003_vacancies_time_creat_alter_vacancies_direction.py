# Generated by Django 4.0.6 on 2022-07-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direction', '0002_alter_direction_parent'),
        ('vacancies', '0002_alter_vacancies_options_vacancies_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancies',
            name='time_creat',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='direction',
            field=models.ManyToManyField(blank=True, null=True, to='direction.direction', verbose_name='Направлениe'),
        ),
    ]
