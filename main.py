from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

class Tutor:
    def __init__(self, nome, email, telefone, idade):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.idade = idade

    def __str__(self):
        return f'\nTutor: {self.nome}\nE-mail: {self.email}\nTelefone: {self.telefone}\nIdade: {self.idade}'
    
class Pet:
    def __init__(self, nome, raca, cor, idade, tutor):
        self.nomepet = nome
        self.racapet = raca
        self.corpet = cor
        self.idadepet = idade
        self.tutor = tutor

    def __str__(self):
        return f'{self.tutor}\n\nPet: {self.nomepet}\nRaça: {self.racapet}\nCor: {self.corpet}\nIdade: {self.idadepet}'

class Agendamento:
   pass

class Agenda:

    def agendar(self):
        pass

    def listar(self):
        pass

lista_cadastro = []

while True:
    menu = ('[gold3]1- Cadastrar tutor e pet\n'
          '2- Agendar\n'
          '3- Listar\n' 
          '4- Sair[/]')
    print(Panel(menu, title='MENU', width=40))

    try:
        op = int(input('Escolha uma opção: '))
        print()
    except ValueError:
        print('Somente números.')
        continue

    if op not in [1, 2, 3, 4]:
        print('Ops, opção inexistente.')

    elif op == 1:
        cadastrotutor = Tutor(Prompt.ask('[chartreuse3]Nome completo[/] '), Prompt.ask('[chartreuse3]E-mail[/] '), Prompt.ask('[chartreuse3]Telefone[/] '), int(Prompt.ask('[chartreuse3]Idade[/] ')))

        cadastropet = Pet(Prompt.ask('\n[chartreuse3]Nome Pet[/] '), Prompt.ask('[chartreuse3]Raça[/] '), Prompt.ask('[chartreuse3]Cor[/] '), int(Prompt.ask('[chartreuse3]Idade Pet[/] ')), cadastrotutor)
        print('[red1]Cadastro criado com sucesso![/]\n')

        lista_cadastro.append(cadastropet)

    elif op == 2:
        pass
    elif op == 3:
        if not lista_cadastro:
            print('[red1]SEM PACIENTES CADASTRADOS[/]')
        else:
            for paciente in lista_cadastro:
                print(Panel(str(paciente), title=f'[chartreuse3]{paciente.nomepet}[/]', width=40))

    elif op == 4:
        print('Saindo...')
        break