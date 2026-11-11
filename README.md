# Agendamento Vet
 
Sistema de agendamento para clínica veterinária, feito em Python e executado no terminal. O projeto nasceu da rotina de recepção de uma clínica veterinária e serve para praticar programação orientada a objetos e a base de um sistema de backend.
 
> Projeto em desenvolvimento.
 
## Funcionalidades
 
**Já funciona**
 
- Menu interativo no terminal, com painel colorido.
- Cadastro de tutor (nome, e-mail, telefone e idade) e do pet dele (nome, raça, cor e idade).
- Listagem dos pacientes cadastrados, cada um em um painel com os dados do pet e do tutor.
- Aviso quando ainda não há pacientes cadastrados.
- Tratamento de erro quando o usuário digita algo que não é número no menu.
**Planejado**
 
- Agendamento de consultas, vacinas e cirurgias para cada pet.
- Salvar os dados em arquivo para não perdê-los ao fechar o programa.
- Banco de dados (SQLite).
- Transformar o sistema em uma API.
## Tecnologias
 
- Python
- [rich](https://github.com/Textualize/rich) para deixar o terminal colorido e organizado
## Como rodar
 
1. Tenha o Python 3 instalado.
2. Instale a biblioteca `rich`:
```
pip install rich
```
 
3. Execute o programa:
```
python main.py
```
 
## Estrutura do código
 
- `Tutor`: guarda os dados do tutor.
- `Pet`: guarda os dados do pet e o tutor ao qual pertence.
- `Agendamento` e `Agenda`: estrutura inicial do agendamento, ainda em construção.
## O que estou praticando
 
- Classes, objetos e o método `__str__`.
- Objetos que guardam outros objetos (o pet guarda o seu tutor).
- Listas e laço `for`.
- Tratamento de erros com `try/except`.
- Uso de bibliotecas externas (`rich`).
- Versionamento com Git e GitHub.