# importando a tipagem List e Dict
from typing import List

# importando biblioteca nativa xml
from xml.etree import ElementTree as ET

# importando a classe Importer que é uma calsse abstrata
# importando a sub classe abstrata Importer
from inventory_report.importer.importer import Importer

# herdando Importer


class XmlImporter(Importer):
    # anotation definindo como método estático pode ser invocado sem ser
    #  instanciado
    @staticmethod
    def import_data(file_name: str) -> List:
        # faz a leitura do caminho do arquivo str caso o final da string
        # não for igual .xml então o arquivo não é válido, pois, a extensão
        # para o metodo aqui implementado é do tipo xml
        if not file_name.endswith(".xml"):
            # dispara um ValueErro que é um caminho inválido
            raise ValueError("Invalid FIle")

        # utilizando um contexto para leitura do arquivo que estou apelidando
        # de xml_file
        with open(file_name, "r") as xml_file:
            # criando minha arvore root
            tree = ET.parse(xml_file)
            root = list(tree.getroot())

            dict_list = []
            info_dict = {}

            for index in range(len(root)):
                for info in root[index]:
                    info_dict[info.tag] = info.text
                dict_list.append(info_dict)
                info_dict = {}

            return dict_list
