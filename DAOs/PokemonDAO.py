import traceback
import psycopg2
from models.Pokemon import Pokemon

class PokemonDAO(object):

    def listarTodos(self):
        resultado = []
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao FROM pokemon")
            registros = cursor.fetchall()
            for linha in registros:
                p = Pokemon()
                p.id = linha[0]
                p.nome = linha[1]
                p.descricao = linha[2]
                p.altura = linha[3]
                p.peso = linha[4]
                p.preco = linha[5]
                p.tipo_1 = linha[6]
                p.tipo_2 = linha[7]
                p.genero_1 = linha[8]
                p.genero_2 = linha[9]
                p.avaliacao = linha[10]
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
            cursor.execute("SELECT id, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao FROM pokemon WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                p = Pokemon()
                p.id = linha[0]
                p.nome = linha[1]
                p.descricao = linha[2]
                p.altura = linha[3]
                p.peso = linha[4]
                p.preco = linha[5]
                p.tipo_1 = linha[6]
                p.tipo_2 = linha[7]
                p.genero_1 = linha[8]
                p.genero_2 = linha[9]
                p.avaliacao = linha[10]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return p

    def inserir(self, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO pokemon (nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao) VALUES ('{}', '{}', {}, {}, {}, '{}', '{}', '{}', '{}', {})".format(nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao))
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

    def atualizar(self, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("UPDATE pokemon SET nome = '{}', descricao = '{}', altura = {}, peso = {}, preco = {}, tipo_1 = '{}', tipo_2 = '{}', genero_1 = '{}', genero_2 = '{}', avaliacao = {} WHERE id = {}".format(nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao, id))
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
            cursor.execute("DELETE FROM pokemon WHERE id = {}".format(id))
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