class SimpleReport:
    # anotation indicando que o metodo é estático
    @staticmethod
    # método de classe generator estatico que recebe como parametro products
    # que é um array de dicionarios com dados referente a empresa
    def generate(products):
        # data de fabricação mais antiga, ou seja, menor valor quando comparda
        # com data atual
        #       |-------------|-------------|
        # 10-08-2022     14-08-2022
        old_manufacture_date = min(el["data_de_fabricacao"] for el in products)
        # Menor data quando comparada com data atual
        data_exp_validate = min(el["data_de_validade"] for el in products)
        # percorrer a lista de dicionário de produto e filtrar o nome
        # das empresas
        company = [el["nome_da_empresa"] for el in products]
        # contar o numero de ocorrencias do nome da emprea retornado
        # na lista company e contar as ocorrencias e pegando a que tiver
        # o maior numero de ocorrencias
        company_count_products = max(set(company), key=company.count)

        return (
            f"Data de fabricação mais antiga: {old_manufacture_date}\n"
            f"Data de validade mais próxima: {data_exp_validate}\n"
            f"Empresa com mais produtos: {company_count_products}\n"
        )


# dict_cadeira = [
#     {
#         "id": 1,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2022-04-04",
#         "data_de_validade": "2023-02-09",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },

#     {
#         "id": 2,
#         "nome_do_produto": "MESA COMPUTADOR",
#         "nome_da_empresa": "Comercial Sao Lourencio",
#         "data_de_fabricacao": "2021-04-04",
#         "data_de_validade": "2023-02-08",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },

#     {
#         "id": 3,
#         "nome_do_produto": "CADEIRA COMPUTADOR",
#         "nome_da_empresa": "Comercial Sao Lourencio",
#         "data_de_fabricacao": "2021-04-04",
#         "data_de_validade": "2023-02-08",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     }


# ]


# simple_report = SimpleReport()

# print(simple_report.generate(dict_cadeira))
