# Generated by Django 5.1.3 on 2024-12-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='option1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='option2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='option3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='option4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='option5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='correct_answer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('choice', 'Выбор ответа')], default='choice', max_length=10),
        ),
    ]
