# Generated by Django 4.1.3 on 2022-11-19 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_alter_student_group_delete_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='journal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.journal'),
        ),
        migrations.AddField(
            model_name='topic',
            name='journal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.journal'),
        ),
        migrations.AddField(
            model_name='topic',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.student'),
        ),
    ]
