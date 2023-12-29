## **API de Gerenciamento de Clientes Agrícolas 

---

🔐 **Autenticação:**
- **Método:** `POST`
- **Endpoint:** `/login`
- **Descrição:** Realiza a autenticação do usuário. Envie um JSON com `username` e `password`. O token JWT retornado será usado para acessar os outros endpoints.

📋 **Obter Todos os Clientes:**
- **Método:** `GET`
- **Endpoint:** `/clientes`
- **Descrição:** Retorna todas as informações dos clientes cadastrados. Requer o cabeçalho `Authorization: Bearer SEU_TOKEN_JWT` para autenticação.

🔍 **Obter Informações de um Cliente Específico:**
- **Método:** `GET`
- **Endpoint:** `/clientes/<string:cliente_nome>`
- **Descrição:** Retorna informações detalhadas do cliente especificado. Substitua `<string:cliente_nome>` pelo nome do cliente desejado. Requer autenticação.

✏️ **Atualizar Informações de um Cliente Específico:**
- **Método:** `PUT`
- **Endpoint:** `/clientes/<string:cliente_nome>`
- **Descrição:** Atualiza as informações do cliente especificado. Substitua `<string:cliente_nome>` pelo nome do cliente desejado. Envie um JSON com os dados a serem atualizados. Requer autenticação.

➕ **Adicionar Novo Cliente:**
- **Método:** `POST`
- **Endpoint:** `/clientes`
- **Descrição:** Adiciona um novo cliente ao sistema. Envie um JSON com os dados do novo cliente. Requer autenticação.

---

🔑 **Autenticação JWT:**
- Para acessar os endpoints `/clientes`, `/clientes/<string:cliente_nome>`, inclua o token JWT no cabeçalho da requisição com a chave `Authorization`.


📌 **Observações:**
- Certifique-se de substituir `SEU_TOKEN_JWT` pelo token JWT obtido no processo de autenticação.
- Recomenda-se o uso de HTTPS em um ambiente de produção para garantir a segurança das informações transmitidas.
