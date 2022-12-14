# Generated by Django 4.1.2 on 2022-10-23 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default='course', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(default='faculty', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='GroupList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default='group', max_length=40)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='third_task.courselist')),
            ],
        ),
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(default='name', max_length=40)),
                ('age', models.IntegerField(default=18)),
                ('type_of_student', models.CharField(default='type', max_length=10)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='third_task.grouplist')),
            ],
        ),
        migrations.AddField(
            model_name='courselist',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='third_task.facultylist'),
        ),
    ]
