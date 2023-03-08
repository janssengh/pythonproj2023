class Produto:

    def __init__(self, descricao, preco, quantidade, id=None):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade = quantidade

    def __str__(self):
        return f'Código: {self.__id} \tDescrição: {self.__descricao} ' \
               f'\tPreço Unitário: R$ {self.__preco} \tQuantidade em Estoque: {self.__quantidade}'

    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade