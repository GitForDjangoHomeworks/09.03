# Generated by Django 4.1.5 on 2023-02-04 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('teachers', '0002_remove_teacher_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ManyToManyField(related_name='subject_teacher', to='subjects.subject'),
        ),
    ]
