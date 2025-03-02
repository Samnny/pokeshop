import traceback
import psycopg2
from models.Publicacao import Publicacao

class PublicacaoDAO(object):

    def listarTodas(self):
        resultado = []
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("SELECT id, data, texto, foto, cliente_id FROM publicacao")
            registros = cursor.fetchall()
            for linha in registros:
                p = Publicacao()
                p.id = linha[0]
                p.data = linha[1]
                p.texto = linha[2]
                p.foto = linha[3]
                p.cliente_id = linha[4]
                resultado.append(p)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    def listar(self, id):
        p = None
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("SELECT id, data, texto, foto, cliente_id FROM publicacao WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                p = Publicacao()
                p.id = linha[0]
                p.data = linha[1]
                p.texto = linha[2]
                p.foto = linha[3]
                p.cliente_id = linha[4]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return p

    def inserir(self, id, data, texto, foto, cliente_id):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO publicacao (id, data, texto, foto, cliente_id) VALUES ('{}', '{}', '{}', '{}', {})".format(id, data, texto, foto, cliente_id))
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

    def atualizar(self, data, texto, foto, cliente_id, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("UPDATE publicacao SET data = '{}', texto = '{}', foto = '{}', cliente_id = {} WHERE id = {}".format(data, texto, foto, cliente_id, id))
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
            cursor.execute("DELETE FROM publicacao WHERE id = {}".format(id))
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
