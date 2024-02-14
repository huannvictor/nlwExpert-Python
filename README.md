# API de Geração de Código de Barras

Esta é uma API desenvolvida durante a Next Level Week (NLW) da Rocketseat, ministrada por Rafael Ferreira, do canal Programador Lhama no YouTube. A API foi construída utilizando Python e Flask, e tem como objetivo gerar códigos de barras de forma simples e eficiente.

## Funcionalidades

- Geração de código de barras a partir de um texto fornecido.
- Suporte a diferentes formatos de código de barras, como EAN-13, Code 39, etc.

## Instalação

Para instalar as dependências do projeto, certifique-se de ter o Python e o pip instalados em seu sistema. Em seguida, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

## Uso
1. Clone este repositório em sua máquina local.
1. Navegue até o diretório do projeto.
1. Execute o arquivo app.py para iniciar o servidor Flask.
1. Acesse a API através do navegador ou de uma ferramenta como Postman, utilizando as rotas disponíveis para gerar códigos de barras.
### Exemplo:
Suponha que você queira gerar um código de barras para o texto "123-456-789".

Você pode fazer uma requisição `GET` para a rota `/barcode/123456789` e a API retornará o código de barras correspondente.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue se encontrar algum problema ou para enviar um pull request com melhorias.

## Licença
Este projeto está licenciado sob a Licença MIT.

