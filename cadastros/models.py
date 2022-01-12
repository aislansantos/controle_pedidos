from django.db import models

# Create your models here.
from django.db import models


class Filial(models.Model):
    descricao = models.CharField(
        verbose_name="Nome da filial",
        max_length=50,
    )

    class Meta:
        db_table = "cad_filial"
        verbose_name = "Filial"
        verbose_name_plural = "Filiais"

    def __str__(self):
        return self.descricao


class Vendedor(models.Model):
    nome = models.CharField(
        verbose_name="Nome do vendedor",
        max_length=50
    )

    class Meta:
        db_table = "cad_vendendor"
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(
        verbose_name="Nome do cliente",
        max_length=250,
    )

    class Meta:
        db_table = "cad_cliente"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome


class Grupo(models.Model):
    descricao = models.CharField(
        verbose_name="Nome do Grupo",
        max_length=50,
    )

    class Meta:
        db_table = "cad_grupo"
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

    def __str__(self):
        return self.descricao


class Fornecedor(models.Model):
    descricao = models.CharField(
        verbose_name="Nome do fornecedor",
        max_length=250,
    )

    class Meta:
        db_table = "cad_fornecedor"
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.descricao


class Produto(models.Model):
    descricao = models.CharField(
        verbose_name="Descrição do Produto",
        max_length=250,
    )

    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.CASCADE,
    )

    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.CASCADE,
    )

    estoque = models.IntegerField(
        verbose_name="Quantidade de produto no estoque",
        default=0,
    )

    class Meta:
        db_table = "cad_produto"
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.descrição