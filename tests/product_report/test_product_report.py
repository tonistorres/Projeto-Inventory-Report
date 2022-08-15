from inventory_report.inventory.product import Product


def test_relatorio_produto():
    # importando a class e fazendo um mock dos seus valores iniciais
    # passando valores ficticios para dos atributos que são carregados
    # e necessitam de valores no momento que é instanciada essa classe
    product = Product(
        100,
        "Agua Sanitaria 1000ml",
        "Almoxarifado Central",
        "01/01/2022",
        "30/01/2025",
        "Serie1234Xlblau",
        "ali",
    )

    str_product = product.__repr__()

    assert str_product == (
        "O produto Agua Sanitaria 1000ml"
        " fabricado em 01/01/2022"
        " por Almoxarifado Central com validade"
        " até 30/01/2025"
        " precisa ser armazenado ali."
    )
