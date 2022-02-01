# Generated by Django 4.0.2 on 2022-02-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('test_input_parameter', models.CharField(max_length=255)),
                ('output_parameter', models.CharField(max_length=255)),
                ('language', models.CharField(choices=[('C#', 'C#'), ('JS', 'JavaScript'), ('PY', 'Python'), ('TS', 'TypeScript'), ('GO', 'Go')], default='PY', max_length=2)),
            ],
        ),
    ]