import unittest

from lab1.loja import Loja
from lab1.gestor import Gestor
from lab1.cliente import Cliente
from lab1.vendedor import Vendedor
from lab1.fatura import Fatura
from lab1.data import Data
from lab1.item import Item

class TestLoja(unittest.TestCase):
    def setUp(self):
        self.gestor = Gestor('Alice','1')
        self.cliente = Cliente('Bob','1')
        self.vendedor = Vendedor('Clara','2')
        self.loja = Loja(self.gestor)

    def criar_cenario(self):
        self.loja.registar_cliente(self.cliente.obter_nome(), self.cliente.obter_numero())
        self.loja.registar_vendedor(self.vendedor.obter_nome(), self.vendedor.obter_numero())
        nomes_itens = [
            "Item 1",
            "Item 2",
            "Item 3",
        ]
        for nome_item in nomes_itens:
            self.loja.registar_item(nome_item)
        
    def test_obter_gestor(self):
        self.assertEqual(self.loja.obter_gestor(), self.gestor)

    def test_obter_vendedores(self):
        self.assertIsInstance(self.loja.obter_vendedores(), list)
        self.loja.registar_vendedor(self.vendedor.obter_nome(), self.vendedor.obter_numero())
        self.assertEquals(self.vendedor.obter_nome(), self.loja.obter_vendedores()[0].obter_nome())

    def test_obter_clientes(self):
        self.assertIsInstance(self.loja.obter_clientes(), list)
        self.loja.registar_cliente(self.cliente.obter_nome(), self.cliente.obter_numero())
        self.assertEquals(self.cliente.obter_nome(), self.loja.obter_clientes()[0].obter_nome())

    def test_obter_items(self):
        self.assertIsInstance(self.loja.obter_itens(), list)

    def test_registar_vendedor(self):
        self.loja.registar_vendedor(self.vendedor.obter_nome(), self.vendedor.obter_numero())
        self.assertEquals(self.vendedor.obter_nome(), self.loja.obter_vendedores()[0].obter_nome())

    def test_registar_gestor(self):
        self.loja.registar_gestor("Novo Gestor","42")
        self.assertEquals(self.loja.obter_gestor().obter_nome(), "Novo Gestor")

    def test_registar_cliente(self):
        self.assertListEqual(self.loja.obter_clientes(), [])
        self.loja.registar_cliente(self.cliente.obter_nome(), self.cliente.obter_numero())
        self.assertEquals(self.cliente.obter_nome(), self.loja.obter_clientes()[0].obter_nome())

    def test_registar_item(self):
        self.assertListEqual(self.loja.obter_itens(), [])
        self.loja.registar_item("Item")
        self.assertIsNotNone(next((item for item in self.loja.obter_itens() if item.obter_nome() == "Item"), None))

    def test_registar_fatura(self):
        self.criar_cenario()
        self.assertListEqual(self.cliente.obter_faturas(), [])
        self.loja.registar_fatura(self.cliente.obter_numero(), self.loja.obter_itens(), self.vendedor.obter_numero(), 2020, 3, 28)
        self.assertEquals(self.loja.obter_faturas_cliente(self.cliente.obter_numero())[0].obter_cliente().obter_nome(), self.cliente.obter_nome())

    def test_obter_faturas_cliente(self):
        self.criar_cenario()
        self.loja.registar_fatura(self.cliente.obter_numero(), self.loja.obter_itens(), self.vendedor.obter_numero(), 2020, 3, 28)
        self.assertEquals(self.loja.obter_faturas_cliente(self.cliente.obter_numero())[0].obter_cliente().obter_nome(), self.cliente.obter_nome())

    def test_obter_faturas_vendedor(self):
        self.criar_cenario()
        self.loja.registar_fatura(self.cliente.obter_numero(), self.loja.obter_itens(), self.vendedor.obter_numero(), 2020, 3, 28)
        self.assertEquals(self.loja.obter_faturas_vendedor(self.vendedor.obter_numero())[0].obter_vendedor().obter_nome(), self.vendedor.obter_nome())

if __name__ == "__main__":
    unittest.main()
