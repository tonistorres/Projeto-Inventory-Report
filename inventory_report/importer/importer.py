# importa a classe base abstrata
from abc import ABC, abstractmethod
# importando o metódo List nativo do python
from typing import List

# Classe Importer ao receber como parâmetro ABC ela se torna uma sub-classe
# de ABC logo se torna abstrata automaticamente por herança.
# que contem em seu escopo um método abstrato que recebe o caminho do tipo
# string mais um raise que obriga a classe que externder Importer a implementar
# esse método como se fosse um contrato obrigatório
# trocados e miúdos podemos dizer que toda e qualquer classe que queria fazer
#  uma importação de arquivo nesse projeto deve herdar por herança a classe
#  abstract Importer que possui o metodo estatico pronto para implementação


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data(file_name: str) -> List:
        raise NotImplementedError
