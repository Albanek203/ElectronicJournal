# Generated by Django 4.1.3 on 2022-11-20 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_remove_student_journal_student_journal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='journal',
        ),
        migrations.CreateModel(
            name='StudentJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.journal')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.student')),
            ],
        ),
    ]
