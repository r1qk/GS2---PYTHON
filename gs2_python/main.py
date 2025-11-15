#Onde o código principal roda
from back import LeadRepository
from recommendation import career
from model import Lead

lead_backend = LeadRepository()

def cadastrar():
    name = input("Digite seu nome: ")
    while True: #Restrição de resposta
        L = input("Digite uma nota para lógica: ")
        A = input("Digite uma nota para adaptabilidade: ")
        CR = input("Digite uma nota para criativdade: ")
        CO = input("Digite uma nota para colaboração: ")

        #Verificando se é número
        opcoes_float = [L, A, CR, CO]
        opcoes_float = [i.replace(".", "") for i in opcoes_float]

        if not (all(i.isnumeric() for i in opcoes_float)):
            print("As entradas devem ser números entre 0 e 10!\n")
        else:
            L, A, CR, CO = float(L), float(A), float(CR), float(CO)
            
            lista = {
                "Lógica": L,
                "Adaptabilidade": A,
                "Criatividade": CR,
                "Colaboração": CO
            }

            #Verificando se os valores são repetidos
            valores = list(lista.values())
            repeticoes = [valores.count(v) for v in set(valores)]
            
            if max(repeticoes) >= 2:
                print("Por favor, dê a mesma nota para afinidades diferentes!\n")
            elif not (0 <= L <= 10 and 0 <= A <= 10 and 0 <= CR <= 10 and 0 <= CO <= 10):
                print("As notas devem ser entre 0 e 10!\n")
            else:
                break
    #selecionando os dois melhores para a análise
    ordem = sorted(lista.items(), key=lambda x: x[1], reverse=True)
    top1, top2 = ordem[0][0], ordem[1][0]
    profissao = career(top1, top2).advice()
    lead = Lead(name, L, CR, CO, A, profissao).model_leads()
    lead_backend.create_lead(lead)
    
    print(f"Profissão recomendada: {profissao}")
    print("Perfil cadastrado e profissão sugerida!\n")

def list_leads():
    leads = lead_backend.read_leads()

    if not leads:
        print("Nenhuma cadastro foi feito no momento!")
        return
    
    print(f'## | {"Nome":<20} | {"Profissão sugerida":<20}') #padroniza espaço

    for i, lead in enumerate(leads):
        print(f'{i:02d} | {lead["name"]:<20} | {lead["recommendation"]:<20}')

def menu():
    print("=== READICT - SISTEMA DE RECOMENDAÇÃO DE PROFISSÕES ===")
    print("A partir de sua nota para certas aptidões, recomendamos uma profissão!")
    print("[1] Cadastrar perfil\n[2] Exibir cadastros\n[3] Sair\n")
    while True:
        opcao = input("Digite o número da ação desejada: ")

        if not (opcao.isnumeric()):
            print("Tente novamente")
        else:
            opcao = int(opcao)
            if opcao > 3 or opcao < 1:
                print("Tente novamente")
            else:
                break

    return opcao

def main():
    while True:
        opcao = menu()
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            list_leads()
            print()
        elif opcao == 3:
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()
