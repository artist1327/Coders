# Generated by Django 2.2.2 on 2019-08-10 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mock_test',
            new_name='Mocktest',
        ),
        migrations.AlterField(
            model_name='mocktest',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.Topics'),
        ),
    ]