class Product:
    def __init__(
        self,
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    ):
        self.id = id
        self.nome_do_produto = nome_do_produto
        self.nome_da_empresa = nome_da_empresa
        # a função str converte em string a data_de_fabricacao
        self.data_de_fabricacao = str(data_de_fabricacao)
        self.data_de_validade = str(data_de_validade)
        self.numero_de_serie = numero_de_serie
        self.instrucoes_de_armazenamento = instrucoes_de_armazenamento
        # retorna a representação do objeto em formato de string

    def __repr__(self):
        return (
            f"O produto {self.nome_do_produto}"
            f" fabricado em {self.data_de_fabricacao}"
            f" por {self.nome_da_empresa} com validade"
            f" até {self.data_de_validade}"
            f" precisa ser armazenado {self.instrucoes_de_armazenamento}."
        )


# agua_sanitaria = Product(
#     100,
#     "Agua Sanitaria 1000ml",
#     "Almoxarifado Central",
#     "01/01/2022",
#     "30/01/2025",
#     "Serie1234Xlblau",
#     "armazene ali",
# )

# resul_metod_repr = agua_sanitaria.__repr__()
# print(resul_metod_repr)
# print("---Testando o tipo----")
# print(type(resul_metod_repr))
# print(type(agua_sanitaria))
# print(agua_sanitaria)
