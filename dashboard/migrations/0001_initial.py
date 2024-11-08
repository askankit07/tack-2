# Generated by Django 5.1.2 on 2024-11-03 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.FloatField(blank=True, null=True)),
                ('likelihood', models.FloatField(blank=True, null=True)),
                ('relevance', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('topics', models.CharField(blank=True, max_length=200, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('sector', models.CharField(blank=True, max_length=100, null=True)),
                ('pest', models.CharField(blank=True, max_length=50, null=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('swot', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
