# fazendo importação do modulo csv para trabalhamos com
# arquivos com esta extensão
import csv
import json
from xml.etree import ElementTree
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

# Verifica qual tipo de arquivo por mieo do metódo
# endswith que verifica os caracteres final da string(caminho)
# para vê se o arquivo termina em .csv, .json, .xml


def data_extracting(path, file):
    if path.endswith(".csv"):
        return receive_csv(file)
    elif path.endswith(".json"):
        return json.load(file)
    elif path.endswith(".xml"):
        return receive_xml(file)


# Se o final da extenão setada pelo metodo data_extracting
# for .csv este método é setado e retorna um dicionario com
# os dados do csv


def receive_csv(file):
    # csv.read retorna um objeto lietor que irá
    # iterar sobre as linhas no arquivo csv fornecido
    headers, *data = csv.reader(file, delimiter=",", quotechar='"')
    return [dict(zip(headers, item)) for item in data]


# Metodo faz a conversão de xml para json


def convertXmlToJson(xml):
    response = {}

    for child in list(xml):
        # se o tamanho da lista for maior que zero
        if len(list(child)) > 0:
            response[child.tag] = convertXmlToJson(child)
        else:
            response[child.tag] = child.text or ""

    return response


# metodo leitura xml e rotorno json


def receive_xml(file):
    root = ElementTree.parse(file).getroot()
    return [convertXmlToJson(record) for record in root.findall("record")]


class Inventory:
    @staticmethod
    def import_data(path, report):
        with open(path, encoding="utf-8") as file:
            result_data = data_extracting(path, file)
            if report == "simples":
                return SimpleReport.generate(result_data)
            if report == "completo":
                return CompleteReport.generate(result_data)
