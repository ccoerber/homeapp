# Generated by Django 2.0.6 on 2018-06-10 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='sensor',
            name='room_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.Location'),
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]