# Generated by Django 4.2.1 on 2023-09-09 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feature',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='town',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='features',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='count',
        ),
        migrations.AddField(
            model_name='apartment',
            name='square',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ApartmentFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rental.apartment')),
                ('feature', models.ManyToManyField(to='Rental.feature')),
            ],
        ),
    ]