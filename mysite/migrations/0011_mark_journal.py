# Generated by Django 4.1.3 on 2022-11-20 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_remove_student_journal_studentjournal'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='journal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.journal'),
        ),
    ]
