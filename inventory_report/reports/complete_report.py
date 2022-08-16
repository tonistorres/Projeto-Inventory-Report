from inventory_report.reports.simple_report import SimpleReport

# classe herda de SimpleReport


class CompleteReport(SimpleReport):
    # metodo estatico recebe uma lista e rtorna uma string
    @staticmethod
    def generate(products_list: list) -> str:
        # criando uma variável que irá receber o retorno do método estático
        # generate contido na classe PAI SimpleReport que recebe como argumento
        # products_list
        result_report_simple = SimpleReport.generate(products_list)
        # criando um dicionario vazio
        dict_product = {}
        # primeiro vou percorrer a lista recebida por parâmetro no método
        # generate
        for product in products_list:

            if product["nome_da_empresa"] in dict_product:
                dict_product[product["nome_da_empresa"]] += 1
            else:
                dict_product[product["nome_da_empresa"]] = 1

        convert_str = CompleteReport.dict_convert_str(dict_product)

        return (
            f"{result_report_simple}\n"
            f"Produtos estocados por empresa:\n"
            f"{convert_str}"
        )

    # converte um dicionario para string
    def dict_convert_str(dict_product):
        # A função str converte o valor especificado em uma string.
        items = str()
        # o método items() retorna um objeto em formato de tuplas contendo
        #  chave valor
        for key, value in dict_product.items():
            items += f"- {key}: {value}\n"
        return items


dict_cadeira = [
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 2,
        "nome_do_produto": "MESA COMPUTADOR",
        "nome_da_empresa": "Comercial Sao Lourencio",
        "data_de_fabricacao": "2021-04-04",
        "data_de_validade": "2023-02-08",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 3,
        "nome_do_produto": "CADEIRA COMPUTADOR",
        "nome_da_empresa": "Comercial Sao Lourencio",
        "data_de_fabricacao": "2021-04-04",
        "data_de_validade": "2023-02-08",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
]


print(CompleteReport.generate(dict_cadeira))
