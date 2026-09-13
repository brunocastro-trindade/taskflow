tarefas = []


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
            print("=== Tarefas ===")

            numero = 1

            for tarefa in tarefas:
                status = "Concluida" if tarefa["concluida"] else "Pendente"
                print(f"{numero} - {tarefa['nome']} ({status})")
                numero += 1

        elif opcao == 3:
            if not tarefas:
                  print("Não existem tarefas cadastradas.")
            else:
                numero_tarefa = int(input("Digite o número da tarefa: "))
                indice = numero_tarefa - 1
                tarefas[indice]["concluida"] = True
                print("Tarefa concluida com sucesso!")     

        elif opcao == 5:
            print("Encerrando o TaskFlow...")
            break
        else:
            print("Opção inválida. Escolha um número de 1 a 5.")