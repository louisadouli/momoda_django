# Generated by Django 4.1.4 on 2023-08-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0016_alter_experiment_catalyst_concentration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment_cta',
            name='cta',
        ),
        migrations.RemoveField(
            model_name='experiment_cta',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='experiment_initiator',
            name='Initiator',
        ),
        migrations.RemoveField(
            model_name='experiment_initiator',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='experiment_monomer',
            name='Monomner',
        ),
        migrations.RemoveField(
            model_name='experiment_monomer',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='experiment_quenchingagent',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='experiment_quenchingagent',
            name='quenching_agent',
        ),
        migrations.RemoveField(
            model_name='experiment_raftagent',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='experiment_raftagent',
            name='raft_agent',
        ),
        migrations.RemoveField(
            model_name='experiment_solvent',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='experiment_solvent',
            name='solvent',
        ),
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
        migrations.DeleteModel(
            name='Experiment_Catalyst',
        ),
        migrations.DeleteModel(
            name='Experiment_Cta',
        ),
        migrations.DeleteModel(
            name='Experiment_Initiator',
        ),
        migrations.DeleteModel(
            name='Experiment_Monomer',
        ),
        migrations.DeleteModel(
            name='Experiment_quenchingagent',
        ),
        migrations.DeleteModel(
            name='Experiment_Raftagent',
        ),
        migrations.DeleteModel(
            name='Experiment_Solvent',
        ),
        migrations.AddField(
            model_name='experiment',
            name='catlyst',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='catalyst', to='experiments.catalyst'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='cta',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='experiments.cta'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='initiator',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='initiator', to='experiments.initiator'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='monomer',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='experiments.monomer'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='quenching_agent',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='quenching_agent', to='experiments.quenchingagent'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='raft_agent',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='raft_agent', to='experiments.raftagent'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='solvent',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='solvent', to='experiments.solvent'),
        ),
    ]
