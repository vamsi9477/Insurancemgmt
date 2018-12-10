# Generated by Django 2.1.1 on 2018-11-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0003_agent_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAgentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.IntegerField(default=5)),
                ('agent_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=5)),
                ('sex', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('repeat_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AdminBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('branch_id', models.IntegerField(default=5)),
                ('branch_name', models.CharField(max_length=50)),
                ('branch_code', models.CharField(max_length=50)),
                ('branch_address', models.CharField(max_length=50)),
                ('branch_location', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('repeat_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AdminOrgModifi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('organisation_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('branch_id', models.IntegerField(default=5)),
                ('branch_code', models.IntegerField(default=5)),
                ('password', models.CharField(max_length=50)),
                ('repeat_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='organisationRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('organsation_name', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=50)),
                ('organsation_address', models.CharField(max_length=500)),
                ('branch_id', models.IntegerField(default=5)),
                ('branch_code', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=50)),
            ],
        ),
    ]
