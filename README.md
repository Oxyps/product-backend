# CRUD de Produtos - BACKEND

## Primeiros passos para rodar o projeto
1. Clonar ou baixar o repositório do [projeto](https://github.com/Oxyps/product-backend);
1. Certificar-se de que já possui o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/installing/) instalado, com o comando no terminal:
	``` shell
		> pip --version
	```
1. Instalar a ferramenta de gerenciamento de ambiente e pacotes [Pipenv](https://pypi.org/project/pipenv/):
	``` shell
		> pip install pipenv
	```
1. Ativar o ambiente:
	``` shell
		> pipenv shell
	```
1. Checar se atende aos requisitos mínimos do projeto:
	``` shell
		> pipenv check
	```
1. Instalar todas as dependências do projeto:
	``` shell
		> pipenv install
		> pipenv install --dev
	```
1. Já dentro do diretório raíz `./product-backend`, rodar as `migrations` para gerar o Banco de Dados:
	``` shell
		> py manage.py migrate
	```
1. Começar a servir a API:
	``` shell
		> py manage.py runserver
	```
1. Rodar o [frontend](https://github.com/Oxyps/product-frontend).

## Rotas

**Produto**
* Listagem e cadastro de produtos (GET e POST): `products/`;
* Detalhe, edição e exclusão de produtos (GET, PUT, DELETE): `products/:product_id/`.

## Tecnologias utilizadas
- [x] [Python](https://docs.python.org/3/)
- [x] [Django Framework](https://docs.djangoproject.com/en/3.1/)
- [x] [Django Rest Framework](https://www.django-rest-framework.org)