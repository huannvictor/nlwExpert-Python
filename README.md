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
2. Navegue até o diretório do projeto.
3. Acesse o ambiente python executando:
  (windows) `.venv\Scripts\activate` 
  (linux/macOs) `.venv\bin\activate`
4. Execute o arquivo `python run.py` para iniciar o servidor Flask.
5. Acesse a API através do navegador ou de uma ferramenta como Postman ou HTTPie, utilizando as rotas disponíveis para gerar códigos de barras.

### Exemplo:
Suponha que você queira gerar um código de barras para o texto "meu-codigo-123".

1. Faça uma requisição `POST` para a rota `/create_tag` 
2. Enviando no body da requisição um JSON:
  ```json
  {
    "product_code": "meu-codigo-123"
  }
  ```
3. a API retornará com o código de barras correspondente.

### Telas de Exemplo:
![tela httpie]('/tela-httpie.png')

![código de barras gerado]('/meu-codigo-123.png')

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue se encontrar algum problema ou para enviar um pull request com melhorias.

## Licença
Este projeto está licenciado sob a Licença MIT.

