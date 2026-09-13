tarefas = []

def listar_tarefas(tarefas):
    print("=== Tarefas ===")
     
    numero = 1
     
    for tarefa in tarefas:
        status = "Concluida" if tarefa["concluida"] else "Pendente"
        print(f"{numero} - {tarefa['nome']} ({status})")
        numero += 1

while True:
        menu = f"""
            ====== TASKFLOW ======

            1 - Criar tarefa
            2 - Listar tarefas
            3 - Concluir tarefa
            4 - Remover tarefa
            5 - Sair

            """
        print(menu)

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
             print("Digite apenas um número.")
             continue
        if opcao == 1:
            nome_tarefa = input("Digite o nome da tarefa: ")

            tarefas.append({
                 "nome": nome_tarefa,
                 "concluida": False
            })

            print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
        
        elif opcao == 2:
             listar_tarefas(tarefas)
        elif opcao == 3:
            if not tarefas:
                  print("Não existem tarefas cadastradas.")
            else:
                try:
                    numero_tarefa = int(input("Digite o número da tarefa: "))
                except ValueError:
                    print("Digite um numero inteiro.")
                    continue
                if numero_tarefa < 1 or numero_tarefa > len(tarefas):
                     print("Essa tarefa não existe.")
                     continue
                indice = numero_tarefa - 1
                tarefas[indice]["concluida"] = True
                print("Tarefa concluida com sucesso!")     
        elif opcao == 4:
            if not tarefas:
                  print("Não existem tarefas cadastradas.")
            else:
                try:
                      numero_tarefa = int(input("Digite o número da tarefa: "))
                except ValueError:
                    print("Digite um numero inteiro.")
                    continue
                if numero_tarefa < 1 or numero_tarefa > len(tarefas):
                    print("Essa tarefa não existe.")
                    continue
                indice = numero_tarefa - 1
                tarefa_removida = tarefas.pop(indice)
                print(f"Tarefa '{tarefa_removida['nome']}' removida com sucesso!")
        elif opcao == 5:
            print("Encerrando o TaskFlow...")
            break
        else:
            print("Opção inválida. Escolha um número de 1 a 5.")