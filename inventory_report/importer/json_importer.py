# fazendo a importação da biblioteca csv nativa do pyton
import json
#  importando List nativo do python
from typing import List
# importando a classe Importer que é uma calsse abstrata
# importando a sub classe abstrata Importer
from inventory_report.importer.importer import Importer

# herdando Importer


class JsonImporter(Importer):
    # implementando o método estatico contrato da classe Importer
    # que retorna do python um tipo List
    @staticmethod
    def import_data(file_name: str) -> List:
        # faz a leitura do caminho do arquivo str caso o final da string
        # não for igual .json então o arquivo não é válido, pois, a extensão
        # para o metodo aqui implementado é do tipo json
        if not file_name.endswith(".json"):
            # dispara um ValueErro que é um caminho inválido
            raise ValueError("Invalid File")

        # utilizando um contexto para leitura do arquivo que estou apelidando
        # de json_file
        with open(file_name, "r") as json_file:
            # retornando o conteudo do arquivo lido json_file
            return json.load(json_file)
