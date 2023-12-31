# Generated by Django 4.1.4 on 2023-08-01 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0017_remove_experiment_cta_cta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='catlyst',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='cta',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='initiator',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='monomer',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='quenching_agent',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='raft_agent',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='solvent',
        ),
        migrations.CreateModel(
            name='Experiment_Solvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.experiment')),
                ('solvent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.solvent')),
            ],
        ),
        migrations.CreateModel(
            name='Experiment_Raftagent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.experiment')),
                ('raft_agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.raftagent')),
            ],
        ),
        migrations.CreateModel(
            name='Experiment_quenchingagent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.experiment')),
                ('quenching_agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.quenchingagent')),
            ],
        ),
        migrations.CreateModel(
            name='Experiment_Monomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monomner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.monomer')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Experiment_Initiator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Initiator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.initiator')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Experiment_Cta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.cta')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Experiment_Catalyst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalyst', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.catalyst')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.experiment')),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='catlyst',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='catalyst', to='experiments.catalyst'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='cta',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='experiments.cta'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='initiator',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='initiator', to='experiments.initiator'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='monomer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='experiments.monomer'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='quenching_agent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quenching_agent', to='experiments.quenchingagent'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='raft_agent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='raft_agent', to='experiments.raftagent'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='solvent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solvent', to='experiments.solvent'),
        ),
    ]
