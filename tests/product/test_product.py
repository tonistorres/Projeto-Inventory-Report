from inventory_report.inventory.product import Product


def test_cria_produto():
    product_mock = Product(
        1,
        "Agua Sanitaria 1000ml",
        "Departamento Almoxarifado",
        "01/01/2022",
        "30/01/2024",
        "x0121tgfer",
        "Armazenar em local...",
    )

    assert product_mock.id == 1
    assert product_mock.nome_do_produto == "Agua Sanitaria 1000ml"
    assert product_mock.nome_da_empresa == "Departamento Almoxarifado"
    assert product_mock.data_de_fabricacao == "01/01/2022"
    assert product_mock.data_de_validade == "30/01/2024"
    assert product_mock.numero_de_serie == "x0121tgfer"
    assert product_mock.instrucoes_de_armazenamento == "Armazenar em local..."
