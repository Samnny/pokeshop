class Venda(object):

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def local_de_entrega(self):
        return self._local_de_entrega

    @local_de_entrega.setter
    def local_de_entrega(self, local_de_entrega):
        self._local_de_entrega = local_de_entrega

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def cliente_id(self):
        return self._cliente_id

    @cliente_id.setter
    def cliente_id(self, cliente_id):
        self._cliente_id = cliente_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
