# Generated by Django 3.0.7 on 2020-06-16 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fertilizer', models.CharField(choices=[('N', 'Nitrogen'), ('P', 'Phosphorus'), ('K', 'Potassium')], default='N', max_length=1)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waterings', to='main_app.Tree')),
            ],
        ),
    ]