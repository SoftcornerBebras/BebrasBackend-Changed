# Generated by Django 3.0 on 2020-06-09 18:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('com', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='option',
            fields=[
                ('optionID', models.AutoField(db_column='optionID', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('questionID', models.AutoField(db_column='questionID', primary_key=True, serialize=False)),
                ('cs_skills', models.CharField(default='default value', max_length=50)),
                ('countryID', models.ForeignKey(db_column='countryID', on_delete=django.db.models.deletion.CASCADE, to='com.Countries')),
                ('domainCodeID', models.ForeignKey(db_column='domainCodeID', on_delete=django.db.models.deletion.CASCADE, related_name='domainCode', to='com.code')),
                ('questionTypeCodeID', models.ForeignKey(db_column='questionTypeCodeID', on_delete=django.db.models.deletion.CASCADE, related_name='questionTypeCode', to='com.code')),
            ],
        ),
        migrations.CreateModel(
            name='questionTranslation',
            fields=[
                ('questionTranslationID', models.AutoField(db_column='questionTranslationID', primary_key=True, serialize=False)),
                ('translation', jsonfield.fields.JSONField()),
                ('modified_on', models.DateField(default=datetime.date(1997, 11, 11))),
                ('modified_by', models.CharField(default='default value', max_length=50)),
                ('Identifier', models.CharField(max_length=50)),
                ('languageCodeID', models.ForeignKey(db_column='languageCodeID', on_delete=django.db.models.deletion.CASCADE, to='com.code')),
                ('questionID', models.ForeignKey(db_column='questionID', on_delete=django.db.models.deletion.CASCADE, to='ques.question')),
            ],
        ),
        migrations.CreateModel(
            name='optionTranslation',
            fields=[
                ('optionTranslationID', models.AutoField(db_column='optionTranslationID', primary_key=True, serialize=False)),
                ('translationO', jsonfield.fields.JSONField()),
                ('languageCodeID', models.ForeignKey(db_column='languageCodeID', on_delete=django.db.models.deletion.CASCADE, to='com.code')),
                ('optionID', models.ForeignKey(db_column='optionID', on_delete=django.db.models.deletion.CASCADE, to='ques.option')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='questionID',
            field=models.ForeignKey(db_column='questionID', on_delete=django.db.models.deletion.CASCADE, to='ques.question'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('ImageID', models.AutoField(db_column='ImageID', primary_key=True, serialize=False)),
                ('ImageName', models.CharField(db_column='ImageName', max_length=50)),
                ('ObjectID', models.IntegerField(db_column='ObjectID')),
                ('uploadedFile', models.CharField(db_column='uploadedFile', max_length=128)),
                ('ImageTypeCodeID', models.ForeignKey(db_column='ImageTypeCodeID', on_delete=django.db.models.deletion.CASCADE, to='com.code')),
            ],
        ),
        migrations.CreateModel(
            name='correctOption',
            fields=[
                ('correctOptionID', models.AutoField(db_column='correctOptionID', primary_key=True, serialize=False)),
                ('ansText', models.CharField(max_length=20, null=True)),
                ('optionTranslationID', models.ForeignKey(db_column='optionTranslationID', null=True, on_delete=django.db.models.deletion.CASCADE, to='ques.optionTranslation')),
                ('questionTranslationID', models.ForeignKey(db_column='questionTranslationID', on_delete=django.db.models.deletion.CASCADE, to='ques.questionTranslation')),
            ],
        ),
    ]
