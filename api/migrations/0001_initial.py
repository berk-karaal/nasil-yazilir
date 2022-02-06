# Generated by Django 4.0.2 on 2022-02-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_spelling', models.CharField(max_length=100)),
                ('wrong_spelling', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('last_use_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_date', models.DateField(null=True)),
                ('words', models.ManyToManyField(to='api.Word')),
            ],
        ),
    ]
