class ComentarioPublicacao(object):

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def texto(self):
        return self._texto

    @texto.setter
    def texto(self, texto):
        self._texto = texto

    @property
    def cliente_id(self):
        return self._cliente_id

    @cliente_id.setter
    def cliente_id(self, cliente_id):
        self._cliente_id = cliente_id

    @property
    def publicacao_id(self):
        return self._publicacao_id

    @publicacao_id.setter
    def publicacao_id(self, publicacao_id):
        self._publicacao_id = publicacao_id
