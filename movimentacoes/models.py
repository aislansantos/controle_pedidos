import django.db.models
import cadastros.models


class PedidoCompra(django.db.models.Model):
    fornecedor = cadastros.models.forenkey(
        cadastros.models.Fornecedor,
        on_delete=django.db.models.CASCADE()
    )

    valor_total_pedido = models.IntergerField(

    )

    class Meta:
        db_table = "pedido_compra"
        verbose_name = 'Pedido de Compra'
        verbose_name_plural = "Pedidos de Compra"

    def __str__(self):
        return self.fornecedor
