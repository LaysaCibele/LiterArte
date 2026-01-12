# LiterArte

O LiterArte é uma plataforma web de gestão de leitura desenvolvida com o framework Django. O objetivo da aplicação é permitir que usuários cataloguem livros, organizem suas listas de leitura pessoais e acompanhem o progresso de suas atividades literárias.

O projeto foca na aplicação de conceitos fundamentais de desenvolvimento web, incluindo arquitetura MTV (Model-Template-View), operações CRUD, autenticação de usuários e design responsivo.

## Funcionalidades Principais

* **Autenticação de Usuários:** Sistema de cadastro, login e logout seguros.
* **Catálogo de Livros:** Visualização de livros cadastrados com detalhes completos (sinopse, autor, capa, dados técnicos).
* **Gestão de Lista de Leitura:** Usuários podem adicionar livros à sua lista pessoal.
* **Status de Leitura:** Atualização dinâmica do status de cada livro (Quero Ler, Lendo, Lido).
* **Remoção de Itens:** Possibilidade de remover livros da lista pessoal.
* **Perfil do Usuário:** Edição de dados cadastrais e preferências literárias.
* **Interface Responsiva:** Layout adaptável para dispositivos móveis (smartphones e tablets) e desktops.

## Tecnologias Utilizadas

### Backend
* **Python 3.11+**: Linguagem principal.
* **Django 5**: Framework web de alto nível.
* **Gunicorn**: Servidor WSGI para produção.
* **Whitenoise**: Gestão de arquivos estáticos em produção.

### Frontend
* **HTML5 & CSS3**: Estrutura semântica e estilização customizada.
* **JavaScript**: Interatividade no menu responsivo e formulários dinâmicos.
* **Django Template Language (DTL)**: Renderização dinâmica de páginas.

### Banco de Dados
* **SQLite**: Utilizado em ambiente de desenvolvimento.
* **PostgreSQL**: Utilizado em ambiente de produção (Render).

### Infraestrutura e Deploy
* **Git**: Controle de versão.
* **Render**: Plataforma de hospedagem em nuvem.

## Pré-requisitos

Para executar este projeto localmente, você precisará ter instalado em sua máquina:
* Python (versão 3.10 ou superior)
* Git

## Como Executar o Projeto Localmente
  1. Baixe o código na sua máquina. Abra o terminal e faça:
      '''bash
            git clone https://github.com/LaysaCibele/LiterArte.git
            cd literarte

  2. Crie o Ambiente Virtual (VENV):
        '''bash
             python -m venv venv
      2.1 Ative o venv:
          '''bash
               venv\Scripts\activate
     2.1.1: Caso esteja no Linux/Mac
           '''bash
                 source venv/bin/activate

   3. Instale as dependências:
            '''bash
                  pip install -r requirements.txt
            
   4. Configure o Banco de Dados:
              '''bash
                    python manage.py runserver

   5. Crie um superusuário para acessar a área de administrador (adicionar livros, usuários, autores, gêneros)
        - ps.: ao criar um superusuário, quando você digitar a senha, por padrão do django, no terminal, não serão exibidos pontos (.....)  nem (******), o campo fica invisível.
               '''bash
                     python manage.py createsuperuser


   6. Rode o servidor:
            '''bash
                  python manage.py runserver
                        - clique no localhost que irá aparecer no seu terminal.

      6.1 Ao rodar o projeto, na barra de endereço, se você quiser acessar o painel de administrador, faça:
                 localhost:8000/admin
                   - você será direcionado para a página de admin do django e poderá acessá-la com o usuário e senha que você criou na 5º etapa (superusuário)




Laysa Cibele - Estudante do 3° período de Ciência da Computação [GitHub: https://github.com/LaysaCibele]

