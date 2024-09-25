# Django Todo List

## Descrição do Projeto

Este é um projeto simples de lista de tarefas (Todo List) construído usando Django, um framework web de alto nível para Python, e Bootstrap, um popular framework de CSS para design responsivo e interfaces de usuário rápidas.

## Funcionalidades

O projeto Django Todo List permite que os usuários:

- Criem tarefas: Adicione novas tarefas à lista de tarefas.
- Visualizem tarefas: Veja todas as tarefas em uma lista organizada.
- Editem tarefas: Modifique detalhes das tarefas existentes.
- Excluam tarefas: Remova tarefas que não são mais necessárias.
- Finalizem tarefas: Marque tarefas como concluídas.

Todas essas funcionalidades são implementadas usando um **CRUD** (Create, Read, Update, Delete) simples, utilizando Django como o backend e Bootstrap para estilização.

## Tecnologias Usadas

- **Python**: Linguagem de programação usada para construir o backend.
- **Django**: Framework web usado para construir o servidor e o gerenciamento de dados.
- **Bootstrap**: Framework de front-end usado para criar uma interface de usuário responsiva e estilizada.
- **HTML/CSS**: Linguagens de marcação e estilo usadas para construir e estilizar a interface do usuário.

## Como Configurar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1. **Clone o Repositório**
- Usando HTTPS:
```bash
git clone https://github.com/htadmg/lista_de_Tarefas.git
```
- Usando SSH:
```bash
git clone git@github.com:htadmg/lista_de_Tarefas.git
```
- Navegue até o diretório do projeto:
```bash
cd .\lista_de_tarefas
```
   
3. **Crie e Ative um Ambiente Virtual (opcional, mas recomendado)**
- **Para Linux/MacOS:**
```bash
python -m venv venv
source venv/bin/activate
```

- **Para Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```   
3. **Instale as dependências**
```bash
pip install -r requirements.txt
```
## Configuração do Banco de Dados

Aplique as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```

### Criação de Superusuário

Para acessar o painel administrativo, crie um superusuário:
```bash
python manage.py createsuperuser
```

### Iniciar o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento com o comando:

```bash
python manage.py runserver
```
### Acessar o Projeto
Abra um navegador e vá para http://127.0.0.1:8000/ para ver o aplicativo em funcionamento. Você pode acessar o painel administrativo em http://127.0.0.1:8000/admin/ usando as credenciais do superusuário que você criou.
