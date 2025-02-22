class Pokemon(object):

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def tipo_1(self):
        return self._tipo_1

    @tipo_1.setter
    def tipo_1(self, tipo_1):
        self._tipo_1 = tipo_1

    @property
    def tipo_2(self):
        return self._tipo_2

    @tipo_2.setter
    def tipo_2(self, tipo_2):
        self._tipo_2 = tipo_2

    @property
    def genero_1(self):
        return self._genero_1

    @genero_1.setter
    def genero_1(self, genero_1):
        self._genero_1 = genero_1

    @property
    def genero_2(self):
        return self._genero_2

    @genero_2.setter
    def genero_2(self, genero_2):
        self._genero_2 = genero_2

    @property
    def avaliacao(self):
        return self._avaliacao

    @avaliacao.setter
    def avaliacao(self, avaliacao):
        self._avaliacao = avaliacao
