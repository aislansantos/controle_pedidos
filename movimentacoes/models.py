from django.db import models
import cadastros.models


class PedidoCompra(models.Model):

    numero_pedido_compra = models.IntegerField(
        verbose_name="Número do Pedido",
        max_length=10,
    )

    fornecedor = models.forenkey(
        cadastros.models.Fornecedor,
        on_delete=models.CASCADE()
    )

    filial = models.forenkey(
        cadastros.models.filial,
        on_delete = models.CASCADE,
    )

    vencimento = models.DateTimeField()



    class Meta:
        db_table = "pedido_compra"
        verbose_name = 'Pedido de Compra'
        verbose_name_plural = "Pedidos de Compra"

    def __str__(self):
        return self.fornecedor
