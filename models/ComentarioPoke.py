class ComentarioPoke(object):

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
    def pokemon_id(self):
        return self._pokemon_id

    @pokemon_id.setter
    def pokemon_id(self, pokemon_id):
        self._pokemon_id = pokemon_id

    @property
    def cliente_id(self):
        return self._cliente_id

    @cliente_id.setter
    def cliente_id(self, cliente_id):
        self._cliente_id = cliente_id
