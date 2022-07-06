# br-med

Projeto feito para o desafio técnico proposto pelo Grupo BR-MED.

## Como rodar:

- Tenha o Python instalado na máquina
- Clone o projeto: `git clone git@github.com:gabrielloliveira/br-med.git`
- Entre na pasta do projeto: `cd br-med/`
- Crie um virtualenv: `python3 -m venv env`
- Ative o virtualenv: `source env/bin/activate`
- Instale as dependências do projeto: `pip install -r requirements.txt`
- Crie um arquivo chamado .env a partir do arquivo env.example: `cp env.example .env`
- Altere as variáveis que você precisa, caso necessário.
- Crie um super-usuário (opcional): `python manage.py createsuperuser`
- Rode o projeto: `python manage.py runserver`

### O projeto está hospedado no Heroku

Acesse https://br-med-gabriell.herokuapp.com/
