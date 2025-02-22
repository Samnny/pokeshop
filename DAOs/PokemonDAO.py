import traceback
import psycopg2
from models import Pokemon

class PokemonDAO(object):

    def listarTodas(self):
        resultado = []
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("SELECT codigo, nome, login, senha FROM pessoa")
            registros = cursor.fetchall()
            for linha in registros:
                p = Pokemon()
                p.codigo = linha[0]
                p.nome = linha[1]
                p.login = linha[2]
                p.senha = linha[3]
                resultado.append(p)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    def listar(self, codigo):
        p = None
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("SELECT codigo, nome, login, senha FROM pessoa WHERE codigo = {}".format(codigo))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                p = Pokemon()
                p.codigo = linha[0]
                p.nome = linha[1]
                p.login = linha[2]
                p.senha = linha[3]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return p

    def inserir(self, nome, login, senha):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO pessoa (nome, login, senha) VALUES ('{}', '{}', '{}')".format(nome, login, senha))
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

    def atualizar(self, nome, login, senha, codigo):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("UPDATE pessoa SET nome = '{}', login = '{}', senha = '{}' WHERE codigo = {}".format(nome, login, senha, codigo))
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

    def remover(self, codigo):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123",
                                          host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM pessoa WHERE codigo = {}".format(codigo))
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