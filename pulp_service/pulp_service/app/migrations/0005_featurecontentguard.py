# Generated by Django 4.2.16 on 2024-11-01 16:55

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import pulpcore.app.models.access_policy


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0125_openpgpdistribution_openpgpkeyring_openpgppublickey_and_more'),
        ('service', '0004_alter_domainorg_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureContentGuard',
            fields=[
                ('headercontentguard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.headercontentguard')),
                ('features', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
            options={
                'permissions': (('manage_roles_featurecontentguard', 'Can manage role assignments on Feature ContentGuard'),),
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.headercontentguard', pulpcore.app.models.access_policy.AutoAddObjPermsMixin),
        ),
    ]