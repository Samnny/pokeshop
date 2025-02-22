import traceback
import psycopg2
from models import Venda

class VendaDAO(object):

    def listarTodas(self):
        resultado = []
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("SELECT id, local_de_entrega, data, cliente_id, status FROM venda")
            registros = cursor.fetchall()
            for linha in registros:
                v = Venda()
                v.id = linha[0]
                v.local_de_entrega = linha[1]
                v.data = linha[2]
                v.cliente_id = linha[3]
                v.status = linha[4]
                resultado.append(v)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    def listar(self, id):
        v = None
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("SELECT id, local_de_entrega, data, cliente_id, status FROM venda WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                v = Venda()
                v.id = linha[0]
                v.local_de_entrega = linha[1]
                v.data = linha[2]
                v.cliente_id = linha[3]
                v.status = linha[4]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return v

    def inserir(self, local_de_entrega, data, cliente_id, status):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO venda (local_de_entrega, data, cliente_id, status) VALUES ('{}', '{}', {}, '{}')".format(local_de_entrega, data, cliente_id, status))
            connection.commit()
            if cursor.rowcount == 1:
                sucesso = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def atualizar(self, local_de_entrega, data, cliente_id, status, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("UPDATE venda SET local_de_entrega = '{}', data = '{}', cliente_id = {}, status = '{}' WHERE id = {}".format(local_de_entrega, data, cliente_id, status, id))
            connection.commit()
            if cursor.rowcount == 1:
                sucesso = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def remover(self, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM venda WHERE id = {}".format(id))
            connection.commit()
            if cursor.rowcount == 1:
                sucesso = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso
