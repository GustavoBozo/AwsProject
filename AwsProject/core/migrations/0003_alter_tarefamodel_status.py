# Generated by Django 4.1.2 on 2022-10-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_tarefamodel_name_alter_tarefamodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefamodel',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'A Fazer'), (2, 'Fazendo'), (3, 'Feito')]),
        ),
    ]