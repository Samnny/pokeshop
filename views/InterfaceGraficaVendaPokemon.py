from models import Pokemon
from DAOs import PokemonDAO
from models import Publicacao
from DAOs import PublicacaoDAO
from models import Venda
from DAOs import VendaDAO
from models import ComentarioPoke
from DAOs import ComentarioPokeDAO
from models import ComentarioPublicacao
from DAOs import ComentarioPublicacaoDAO

class InterfaceGraficaVendaPokemon(object):

    # Menu principal
    def menu_principal(self):
        print("=============================")
        print("Sistema de Venda de Pokémons")
        print("=============================")
        print("1 - Cadastro de Pokémons     ")
        print("2 - Cadastro de Publicações  ")
        print("3 - Vendas de Pokémons       ")
        print("4 - Comentários de Pokes     ")
        print("5 - Comentários de Publicações")
        print("0 - Sair                     ")
        print("=============================")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 1:
            self.menu_cadastro_poke()
            return
        if opcao == 2:
            self.menu_cadastro_publicacao()
            return
        if opcao == 3:
            self.menu_venda_pokemon()
            return
        if opcao == 4:
            self.menu_cadastro_comentario_poke()
            return
        if opcao == 5:
            self.menu_cadastro_comentario_publicacao()
            return
        if opcao == 0:
            return
        self.menu_principal()

    # Menu de Cadastro de Pokes
    def menu_cadastro_poke(self):
        print("===========================")
        print("Cadastro de Pokémons       ")
        print("===========================")
        print("1 - Listar Todos os Pokémons")
        print("2 - Listar um Pokémon       ")
        print("3 - Inserir um Pokémon      ")
        print("4 - Atualizar um Pokémon    ")
        print("5 - Remover um Pokémon      ")
        print("0 - Voltar                  ")
        print("===========================")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 1:
            self.menu_listar_todos_pokes()
            return
        if opcao == 2:
            self.menu_listar_um_poke()
            return
        if opcao == 3:
            self.menu_inserir_um_poke()
            return
        if opcao == 4:
            self.menu_atualizar_um_poke()
            return
        if opcao == 5:
            self.menu_remover_um_poke()
            return
        if opcao == 0:
            self.menu_principal()
            return
        self.menu_cadastro_poke()

    # Menu de Cadastro de Publicações
    def menu_cadastro_publicacao(self):
        print("===========================")
        print("Cadastro de Publicações    ")
        print("===========================")
        print("1 - Listar Todas as Publicações")
        print("2 - Listar uma Publicação    ")
        print("3 - Inserir uma Publicação   ")
        print("4 - Atualizar uma Publicação ")
        print("5 - Remover uma Publicação   ")
        print("0 - Voltar                   ")
        print("===========================")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 1:
            self.menu_listar_todas_publicacoes()
            return
        if opcao == 2:
            self.menu_listar_uma_publicacao()
            return
        if opcao == 3:
            self.menu_inserir_uma_publicacao()
            return
        if opcao == 4:
            self.menu_atualizar_uma_publicacao()
            return
        if opcao == 5:
            self.menu_remover_uma_publicacao()
            return
        if opcao == 0:
            self.menu_principal()
            return
        self.menu_cadastro_publicacao()

    # Menu de Vendas de Pokémons
    def menu_venda_pokemon(self):
        print("=============================")
        print("Vendas de Pokémons          ")
        print("=============================")
        print("1 - Listar Vendas           ")
        print("2 - Realizar Venda          ")
        print("0 - Voltar                  ")
        print("=============================")
        opcao = int(input("Digite uma opção [0-2]: "))
        if opcao == 1:
            self.menu_listar_vendas()
            return
        if opcao == 2:
            self.menu_realizar_venda()
            return
        if opcao == 0:
            self.menu_principal()
            return
        self.menu_venda_pokemon()

    # Menu de Cadastro de Comentários de Poke
    def menu_cadastro_comentario_poke(self):
        print("===============================")
        print("Cadastro de Comentários de Poke")
        print("===============================")
        print("1 - Listar Todos os Comentários de Poke")
        print("2 - Listar um Comentário de Poke")
        print("3 - Inserir um Comentário de Poke")
        print("4 - Atualizar um Comentário de Poke")
        print("5 - Remover um Comentário de Poke")
        print("0 - Voltar")
        print("===============================")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 1:
            self.menu_listar_todos_comentarios_poke()
            return
        if opcao == 2:
            self.menu_listar_um_comentario_poke()
            return
        if opcao == 3:
            self.menu_inserir_um_comentario_poke()
            return
        if opcao == 4:
            self.menu_atualizar_um_comentario_poke()
            return
        if opcao == 5:
            self.menu_remover_um_comentario_poke()
            return
        if opcao == 0:
            self.menu_principal()
            return
        self.menu_cadastro_comentario_poke()

    # Menu de Cadastro de Comentários de Publicação
    def menu_cadastro_comentario_publicacao(self):
        print("===============================")
        print("Cadastro de Comentários de Publicação")
        print("===============================")
        print("1 - Listar Todos os Comentários de Publicação")
        print("2 - Listar um Comentário de Publicação")
        print("3 - Inserir um Comentário de Publicação")
        print("4 - Atualizar um Comentário de Publicação")
        print("5 - Remover um Comentário de Publicação")
        print("0 - Voltar")
        print("===============================")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 1:
            self.menu_listar_todos_comentarios_publicacao()
            return
        if opcao == 2:
            self.menu_listar_um_comentario_publicacao()
            return
        if opcao == 3:
            self.menu_inserir_um_comentario_publicacao()
            return
        if opcao == 4:
            self.menu_atualizar_um_comentario_publicacao()
            return
        if opcao == 5:
            self.menu_remover_um_comentario_publicacao()
            return
        if opcao == 0:
            self.menu_principal()
            return
        self.menu_cadastro_comentario_publicacao()

    # Métodos para listar e inserir as entidades de Pokémons, Publicações, Vendas, Comentários...
    def menu_listar_todos_pokes(self):
        dao = PokeDAO()
        print("Listando Todos os Pokémons...")
        pokes = dao.listarTodas()
        for p in pokes:
            print("ID = {} - Nome = {} - Preço = {}".format(p.id, p.nome, p.preco))
        self.menu_cadastro_poke()

    def menu_listar_todas_publicacoes(self):
        dao = PublicacaoDAO()
        print("Listando Todas as Publicações...")
        publicacoes = dao.listarTodas()
        for p in publicacoes:
            print("ID = {} - Texto = {}".format(p.id, p.texto))
        self.menu_cadastro_publicacao()

    def menu_realizar_venda(self):
        dao_poke = PokeDAO()
        dao_venda = VendaDAO()

        poke_id = int(input("Digite o ID do Pokémon: "))
        poke = dao_poke.listar(poke_id)
        if not poke:
            print("Pokémon não encontrado!")
            return
        cliente_id = int(input("Digite o ID do Cliente: "))
        quantidade = int(input("Digite a quantidade que deseja vender: "))
        sucesso = dao_venda.inserir(poke_id, cliente_id, quantidade)
        if sucesso:
            print("Venda realizada com sucesso!")
        else:
            print("Falha ao realizar a venda.")
        self.menu_venda_pokemon()

    def menu_listar_vendas(self):
        dao = VendaDAO()
        print("Listando todas as Vendas...")
        vendas = dao.listarTodas()
        for v in vendas:
            print("ID = {} - Pokémon ID = {} - Cliente ID = {} - Quantidade = {}".format(v.id, v.poke_id, v.cliente_id,
                                                                                         v.quantidade))
        self.menu_venda_pokemon()

# Inicializa a aplicação
if __name__ == '__main__':
    gui = InterfaceGraficaVendaPokemon()
    gui.menu_principal()
