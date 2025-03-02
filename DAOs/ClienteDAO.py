import traceback
import psycopg2
from models.Cliente import Cliente

class ClienteDAO(object):

    def listarTodas(self):
        resultado = []
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, cpf, endereco FROM cliente")
            registros = cursor.fetchall()
            for linha in registros:
                c = Cliente()
                c.id = linha[0]
                c.nome = linha[1]
                c.cpf = linha[2]
                c.endereco = linha[3]
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
            cursor.execute("SELECT id, nome, cpf, endereco FROM cliente WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                c = Cliente()
                c.id = linha[0]
                c.nome = linha[1]
                c.cpf = linha[2]
                c.endereco = linha[3]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return c

    def inserir(self, id, nome, cpf, endereco):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO cliente (id, nome, cpf, endereco) VALUES ('{}', '{}', '{}', '{}')".format(id, nome, cpf, endereco))
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

    def atualizar(self, nome, cpf, endereco, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()
            cursor.execute("UPDATE cliente SET nome = '{}', cpf = '{}', endereco = '{}' WHERE id = {}".format(nome, cpf, endereco, id))
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
            cursor.execute("DELETE FROM cliente WHERE id = {}".format(id))
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

    def verificar_cliente(self, email, senha):
        cliente = None
        connection = None
        cursor = None
        try:
            connection = psycopg2.connect(user="postgres", password="123",
                                          host="localhost", port="5432", database="pokemon")
            cursor = connection.cursor()

            query = "SELECT id, nome, cpf, endereco FROM cliente WHERE email = %s AND senha = %s"
            cursor.execute(query, (email, senha))

            row = cursor.fetchone()

            if row:
                cliente = Cliente()
                cliente.id = row[0]
                cliente.nome = row[1]
                cliente.cpf = row[2]
                cliente.endereco = row[3]

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return cliente