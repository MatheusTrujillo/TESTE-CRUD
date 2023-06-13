class GerenciadorTarefas:
    STATUS_PENDENTE = 'P'
    STATUS_CONCLUIDO = 'C'

    def __init__(self):
        self.tarefas = []

    def criar_tarefa(self):
        tarefa_titulo = input("Digite o título da tarefa a ser criada: ")
        while not tarefa_titulo:
            tarefa_titulo = input("Digite o título da tarefa: ")

        tarefa_descricao = input("Digite a descrição da tarefa: ")
        while not tarefa_descricao:
            tarefa_descricao = input("Digite a descrição da tarefa: ")

        tarefa_status = self.validar_status_tarefa()

        tarefa = {
            'tarefa': tarefa_titulo,
            'descricao': tarefa_descricao,
            'status': tarefa_status
        }

        self.tarefas.append(tarefa)
        print("Tarefa criada com sucesso!")

    def consultar_tarefas(self):
        if not self.tarefas:
            print("Não há tarefas.")
        else:
            print("Tarefas:")
            for tarefa in self.tarefas:
                print("Tarefa:", tarefa['tarefa'])
                print("Descrição:", tarefa['descricao'])
                print("Status:", tarefa['status'])
                print()

    def atualizar_tarefa(self):
        tarefa_desejada = input("Digite o título da tarefa que deseja atualizar: ")

        encontrado = False

        for tarefa in self.tarefas:
            if tarefa['tarefa'] == tarefa_desejada:
                novo_titulo = input("Digite o novo título da tarefa (ou deixe em branco para manter o atual): ")
                novo_descricao = input("Digite a nova descrição da tarefa (ou deixe em branco para manter a atual): ")
                novo_status = self.validar_status_tarefa()

                if novo_titulo:
                    tarefa['tarefa'] = novo_titulo
                if novo_descricao:
                    tarefa['descricao'] = novo_descricao
                if novo_status:
                    tarefa['status'] = novo_status

                encontrado = True
                print("Tarefa atualizada com sucesso!")
                break

        if not encontrado:
            print("Tarefa não encontrada.")

    def excluir_tarefa(self):
        tarefa_desejada = input("Digite o título da tarefa que deseja excluir: ")

        encontrado = False
        for tarefa in self.tarefas:
            if tarefa['tarefa'] == tarefa_desejada:
                self.tarefas.remove(tarefa)
                encontrado = True
                print("Tarefa excluída com sucesso.")
                break
        if not encontrado:
            print("Tarefa não encontrada.")

    @staticmethod
    def validar_status_tarefa():
        while True:
            tarefa_status = input("Digite o status da tarefa ('C' para concluída, 'P' para pendente): ").lower()
            if tarefa_status == GerenciadorTarefas.STATUS_CONCLUIDO.lower() or tarefa_status == GerenciadorTarefas.STATUS_PENDENTE.lower():
                return tarefa_status
            else:
                print("Status inválido. Digite 'C' para concluída ou 'P' para pendente.")


gerenciador = GerenciadorTarefas()

while True:
    print("** GERENCIADOR DE TAREFAS **")
    print("Selecione uma opção:")
    print("1 - Criar nova tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Atualizar tarefas")
    print("4 - Excluir tarefas")
    print("5 - Sair")

    opcao = input("Opção selecionada: ")

    if opcao == '1':
        gerenciador.criar_tarefa()
    elif opcao == '2':
        gerenciador.consultar_tarefas()
    elif opcao == '3':
        gerenciador.atualizar_tarefa()
    elif opcao == '4':
        gerenciador.excluir_tarefa()
    elif opcao == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Digite uma opção válida.")
