import traceback
import psycopg2
from models import ComentarioPublicacao

class ComentarioPublicacaoDAO(object):

    def listarTodos(self):
        resultado = []
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("SELECT id, data, texto, cliente_id, publicacao_id FROM comentario_publicacao")
            registros = cursor.fetchall()
            for linha in registros:
                c = ComentarioPublicacao()
                c.id = linha[0]
                c.data = linha[1]
                c.texto = linha[2]
                c.cliente_id = linha[3]
                c.publicacao_id = linha[4]
                resultado.append(c)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    def listar(self, id):
        c = None
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("SELECT id, data, texto, cliente_id, publicacao_id FROM comentario_publicacao WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                c = ComentarioPublicacao()
                c.id = linha[0]
                c.data = linha[1]
                c.texto = linha[2]
                c.cliente_id = linha[3]
                c.publicacao_id = linha[4]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return c

    def inserir(self, data, texto, cliente_id, publicacao_id):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO comentario_publicacao (data, texto, cliente_id, publicacao_id) VALUES ('{}', '{}', {}, {})".format(data, texto, cliente_id, publicacao_id))
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

    def atualizar(self, data, texto, cliente_id, publicacao_id, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("UPDATE comentario_publicacao SET data = '{}', texto = '{}', cliente_id = {}, publicacao_id = {} WHERE id = {}".format(data, texto, cliente_id, publicacao_id, id))
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
            cursor.execute("DELETE FROM comentario_publicacao WHERE id = {}".format(id))
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
