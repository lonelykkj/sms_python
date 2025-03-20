# Envio de SMS com Twilio usando FastAPI

Este projeto demonstra como integrar o **FastAPI** com a API de envio de SMS da **Twilio**. A API oferece um endpoint para enviar mensagens SMS de forma simples, utilizando a Twilio API.

## Tecnologias Usadas

- **FastAPI**: Framework moderno para construção de APIs em Python.
- **Twilio**: Serviço de comunicação para envio de SMS e outras funcionalidades.
- **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI.

## Código da Aplicação

A aplicação tem um único endpoint, que permite enviar SMS através da API da Twilio.

### Estrutura do Código

```python
# Importa o FastAPI e HTTPException do módulo fastapi para criar a API e lidar com exceções HTTP
from fastapi import FastAPI, HTTPException
# Importa o Client da Twilio para interagir com a API de envio de SMS
from twilio.rest import Client

# Cria a instância principal do FastAPI
app = FastAPI()

# Variáveis que armazenam as credenciais da Twilio e o número de telefone usado para enviar mensagens
# Substitua esses valores pelos seus dados reais da conta da Twilio
ACCOUNT_SID = 'twiolio account sid'  # SID da sua conta Twilio
AUTH_TOKEN = 'twilio auth token'     # Token de autenticação da sua conta Twilio
PHONE_NUMBER = 'twilio number'       # Número Twilio de onde as mensagens serão enviadas

# Cria o cliente Twilio usando o SID e o token de autenticação
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Define o endpoint POST "/send-sms/", que será usado para enviar SMS
@app.post("/send-sms/")
async def send_sms(to: str, body: str):
    """
    Este endpoint recebe dois parâmetros:
    - 'to': Número de telefone do destinatário.
    - 'body': Corpo da mensagem que será enviada.

    O Twilio Client é utilizado para enviar um SMS para o número especificado.
    Se o envio for bem-sucedido, retornamos um status de sucesso.
    Caso contrário, um erro é gerado.
    """
    try:
        # Cria e envia a mensagem SMS via Twilio
        # A mensagem é enviada de um número Twilio (PHONE_NUMBER) para o número fornecido no parâmetro 'to'
        # O corpo da mensagem é passado no parâmetro 'body'
        message = client.messages.create(
            from_=PHONE_NUMBER,  # Número Twilio de envio
            to=to,               # Número do destinatário
            body=body            # Corpo da mensagem
        )

        # Retorna um status de sucesso com o SID da mensagem enviada
        return {'status': 'success', 'message_sid': message.sid}
    except Exception as e:
        # Em caso de erro, levanta uma exceção HTTP com o código de status 500 (Erro Interno do Servidor)
        # A mensagem de erro será a descrição do erro gerado
        raise HTTPException(status_code=500, detail=str(e))
```

### Explicação do Código

1. **Imports**:
   - `FastAPI`: Usado para criar a aplicação e os endpoints da API.
   - `HTTPException`: Usado para capturar e retornar erros HTTP de forma personalizada.
   - `Client`: Usado para se comunicar com a API Twilio para enviar SMS.

2. **Configurações da Twilio**:
   - **`ACCOUNT_SID`**: O SID da sua conta Twilio. Você pode obter isso ao criar uma conta na Twilio.
   - **`AUTH_TOKEN`**: O token de autenticação gerado pela Twilio. Ele é necessário para autenticar as requisições.
   - **`PHONE_NUMBER`**: O número de telefone Twilio de onde os SMS serão enviados.

3. **Instância do Cliente Twilio**:
   - `client = Client(ACCOUNT_SID, AUTH_TOKEN)`: Cria uma instância do cliente Twilio, autenticando com o **Account SID** e o **Auth Token**.

4. **Endpoint `/send-sms/`**:
   - Este endpoint é acessado via **POST** e espera dois parâmetros no corpo da requisição:
     - **`to`**: O número de telefone do destinatário (em formato internacional, como `+152387674396`).
     - **`body`**: O texto da mensagem que será enviada.
   
   - A função tenta criar a mensagem e enviá-la usando o `client.messages.create()`.
   - Se o envio for bem-sucedido, a função retorna um status **success** com o **message_sid** (identificador único da mensagem).
   - Se ocorrer algum erro, a função retorna um **HTTPException** com um código de erro 500 e uma descrição do erro.

### Como Usar

1. **Configuração**:
   - Obtenha suas credenciais da Twilio (Account SID, Auth Token e número Twilio).
   - Substitua os valores de `ACCOUNT_SID`, `AUTH_TOKEN` e `PHONE_NUMBER` no código pelas suas credenciais.

2. **Rodando o servidor**:
   Se você estiver usando **Poetry** para gerenciar o ambiente, execute o seguinte comando para rodar o servidor:

   ```bash
   poetry run uvicorn main:app --reload
   ```

   A API estará disponível em `http://127.0.0.1:8000`.

3. **Fazendo uma requisição**:
   Você pode testar a API usando **Postman** ou **curl**.

   **Exemplo com `curl`**:

   ```bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/send-sms/' \
     -H 'Content-Type: application/json' \
     -d '{
     "to": "your number",
     "body": "Esta é uma mensagem de teste!"
   }'
   ```

   Se tudo correr bem, você receberá uma resposta como esta:

   ```json
   {
     "status": "success",
     "message_sid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
   }
   ```

### Possíveis Melhorias

- **Autenticação**: Adicionar autenticação para garantir que apenas usuários autorizados possam enviar SMS.
- **Configuração com variáveis de ambiente**: Utilizar um arquivo `.env` para armazenar as credenciais da Twilio e outras configurações sensíveis.
- **Testes automatizados**: Criar testes com **pytest** para garantir que o envio de SMS e o tratamento de erros funcionem corretamente.
- **Logs**: Implementar logs para monitoramento de falhas e envios bem-sucedidos.
