# Generated by Django 5.0.4 on 2024-04-11 04:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuracoes', '0001_initial'),
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RendaFixaTipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=128)),
                ('fgc', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RendaFixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=128)),
                ('rentabilidade_pre', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('rentabilidade_pos', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='contas.conta')),
                ('emissor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='contas.instituicao')),
                ('rentabilidade_pos_indexador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='configuracoes.indexadores')),
                ('renda_fixa_tipo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ativos.rendafixatipo')),
            ],
        ),
    ]