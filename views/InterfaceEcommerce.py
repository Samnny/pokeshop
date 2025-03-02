import uuid
from datetime import datetime
from DAOs.ClienteDAO import ClienteDAO
from DAOs.VendaDAO import VendaDAO
from DAOs.PokemonDAO import PokemonDAO
from DAOs.PublicacaoDAO import PublicacaoDAO
from DAOs.ComentarioPokeDAO import ComentarioPokeDAO
from DAOs.ComentarioPublicacaoDAO import ComentarioPublicacaoDAO



class InterfaceEcommerce:
    def __init__(self):
        self.cliente_dao = ClienteDAO()
        self.venda_dao = VendaDAO()
        self.pokemon_dao = PokemonDAO()
        self.publicacaoDAO = PublicacaoDAO()
        self.comentarioPublicacaoDAO = ComentarioPublicacaoDAO()
        self.comentarioPokeDAO = ComentarioPokeDAO()
        self.usuario_logado = None
        self.carrinho = []

    def menu_principal(self):
        while True:
            print("\n========================")
            print("Bem-vindo ao E-commerce de Pokémons!")
            print("========================")
            print("1 - Entrar")
            print("2 - Cadastrar Cliente")
            print("3 - Listar Pokémons")
            print("4 - Ver Carrinho")
            print("5 - Finalizar Compra")
            print("6 - Feed de Publicações")
            print("7 - Publicar Novo Conteúdo")
            print("0 - Sair")
            print("========================")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.login()
            elif opcao == "2":
                self.cadastrar_cliente()
            elif opcao == "3":
                self.listar_pokemons()
            elif opcao == "4":
                self.ver_carrinho()
            elif opcao == "5":
                self.finalizar_compra()
            elif opcao == "6":
                self.exibir_feed_publicacoes()
            elif opcao == "7":
                self.adicionar_publicacao_menu()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

    def login(self):
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")

        cliente = self.cliente_dao.verificar_cliente(email, senha)
        if cliente:
            print(f"Bem-vindo {cliente.nome}!")
            self.usuario_logado = cliente
            self.menu_compras()
        else:
            print("Cliente não encontrado ou senha incorreta.")

    def cadastrar_cliente(self):
        id = uuid.uuid4().int % (2**31 - 1)
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF: ")
        endereco = input("Digite seu endereço: ")
        sucesso = self.cliente_dao.inserir(id, nome, cpf, endereco)

        if sucesso:
            print(f"Cliente {nome} cadastrado com sucesso!")
        else:
            print("Erro ao cadastrar cliente.")

    def listar_pokemons(self):
        print("\nListando todos os Pokémons disponíveis:")
        pokemons = self.pokemon_dao.listarTodos()

        if not pokemons:
            print("Nenhum Pokémon disponível.")
        else:
            for p in pokemons:
                print(f"{p.id} - {p.nome}: {p.preco} Reais")

        self.menu_compras()

    def adicionar_ao_carrinho(self):
        if not self.usuario_logado:
            print("Você precisa estar logado para adicionar itens ao carrinho.")
            return

        try:
            pokemon_id = int(input("Digite o ID do Pokémon para adicionar ao carrinho: "))
            quantidade = int(input("Digite a quantidade: "))
            pokemon = self.pokemon_dao.listar(pokemon_id)

            if pokemon:
                self.carrinho.append({"pokemon": pokemon, "quantidade": quantidade})
                print(f"{quantidade} de {pokemon.nome} foram adicionados ao carrinho.")
            else:
                print("Pokémon não encontrado!")
        except ValueError:
            print("Por favor, insira valores válidos.")

    def menu_compras(self):
        while True:
            print("\n========================")
            print("Menu de Compras")
            print("========================")
            print("1 - Listar Pokémons")
            print("2 - Adicionar ao Carrinho")
            print("3 - Ver Carrinho")
            print("4 - Finalizar Compra")
            print("0 - Voltar")
            print("========================")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.listar_pokemons()
            elif opcao == "2":
                self.adicionar_ao_carrinho()
            elif opcao == "3":
                self.ver_carrinho()
            elif opcao == "4":
                self.finalizar_compra()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

    def ver_carrinho(self):
        if not self.carrinho:
            print("Seu carrinho está vazio.")
        else:
            print("\nSeu Carrinho de Compras:")
            total = 0
            for item in self.carrinho:
                subtotal = item["pokemon"].preco * item["quantidade"]
                total += subtotal
                print(f"{item['pokemon'].nome} - Quantidade: {item['quantidade']} - Preço: {subtotal} Reais")

            print(f"Total: {total} Reais")

    def finalizar_compra(self):
        if not self.usuario_logado:
            print("Você precisa estar logado para finalizar a compra.")
            return

        if not self.carrinho:
            print("Seu carrinho está vazio, não há o que comprar.")
            return

        print("\nFinalizando compra...")
        total = sum(item["pokemon"].preco * item["quantidade"] for item in self.carrinho)
        print(f"Total da compra: {total} Reais")

        local_entrega = input("Digite o local de entrega: ")
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        id = uuid.uuid4().int % (2**31 - 1)
        pokemon_vendas = [(item["pokemon"].id, item["quantidade"]) for item in self.carrinho]

        sucesso = self.venda_dao.inserir(id, local_entrega, data, self.usuario_logado.id, pokemon_vendas)
        if sucesso:
            print("Compra realizada com sucesso!")
            self.carrinho = []
        else:
            print("Erro ao finalizar compra.")

    def exibir_feed_publicacoes(self):
        print("\nFeed de Publicações:")
        publicacoes = self.publicacaoDAO.listarTodas()
        if not publicacoes:
            print("Nenhuma publicação encontrada.")
        else:
            for pub in publicacoes:
                print(f"{pub.data} - {pub.texto} (por Cliente {pub.cliente_id})")
                comentarios = self.comentarioPublicacaoDAO.listar(pub.id)
                if comentarios:
                    for comentario in comentarios:
                        print(f"  Comentário: {comentario.texto} (por Cliente {comentario.cliente_id})")
                else:
                    print("  Nenhum comentário nesta publicação.")

    def adicionar_publicacao_menu(self):
        if not self.usuario_logado:
            print("Você precisa estar logado para publicar.")
            return

        print("\nAdicionando uma nova publicação...")
        texto = input("Digite o texto da publicação: ")
        foto = input("Digite o link para a foto (ou deixe em branco): ")
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cliente_id = self.usuario_logado.id

        id = uuid.uuid4().int % (2**31 - 1)
        sucesso = self.adicionar_publicacao(id, data, texto, foto, cliente_id)
        if sucesso:
            print("Publicação realizada com sucesso!")
        else:
            print("Erro ao realizar a publicação.")

    def adicionar_publicacao(self, id, data, texto, foto, cliente_id):
        return self.publicacaoDAO.inserir(id, data, texto, foto, cliente_id)

    def adicionar_comentario_publicacao(self, data, texto, cliente_id, publicacao_id):
        return self.comentarioPublicacaoDAO.inserir(data, texto, cliente_id, publicacao_id)

    def adicionar_comentario_pokemon(self, data, texto, pokemon_id, cliente_id):
        return self.comentarioPokeDAO.inserir(data, texto, pokemon_id, cliente_id)


# Executando a Interface
if __name__ == "__main__":
    interface = InterfaceEcommerce()
    interface.menu_principal()
