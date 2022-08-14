# fazendo a importação da biblioteca csv nativa do pyton
import csv
#  importando List nativo do python
from typing import List
# importando a classe Importer que é uma calsse abstrata
# importando a sub classe abstrata Importer
from inventory_report.importer.importer import Importer

# herdando Importer


class CsvImporter(Importer):
    # implementando o método estatico contrato da classe Importer
    # que retorna do python um tipo List
    @staticmethod
    def import_data(file_name: str) -> List:
        # faz a leitura do caminho do arquivo str caso o final da string
        # não for igual .csv então o arquivo não é válido, pois, a extensão
        # para o metodo aqui implementado é do tipo csv
        if not file_name.endswith(".csv"):
            # dispara um ValueErro que é um caminho inválido
            raise ValueError("Invalid File")

        # utilizando um contexto para leitura do arquivo que estou apelidando
        # de csv_file
        with open(file_name, "r") as csv_file:
            # estu declarando uma variavel reader para receber o retorno do
            # método DictRead ao fazer a leitura do arquivo
            reader = csv.DictReader(csv_file)
            # return o arquivo lido em forma de lista
            return list(reader)
