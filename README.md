# Upload de Arquivos para API

Este projeto é um script em Python que faz o upload de arquivos de uma pasta local para uma API. Ele também registra os nomes dos arquivos que falharam durante o processo de upload em um arquivo de texto.

## Funcionalidades

- **Upload de Arquivos**: Envia arquivos de uma pasta local para um endpoint de API usando requisições POST.
- **Registro de Erros**: Salva os nomes dos arquivos que falharam no upload em um arquivo de texto (`files_with_error.txt`).
- **Verificação de Pasta**: Verifica se a pasta local existe antes de iniciar o processo.

## Pré-requisitos

- Python 3.x instalado.
- Bibliotecas Python necessárias: `requests`.

## Como Usar

### 1. Instalação

Clone este repositório ou baixe o script Python.

### 2. Configuração

1. **Endpoint da API**:

   - Atualize a variável `UPLOAD_URL` no script com o endpoint da sua API:
     ```python
     UPLOAD_URL = "http://localhost:3000/questao/upload"
     ```

2. **Pasta Local**:

   - Coloque os arquivos que deseja enviar na pasta `./planilhas` (ou atualize o caminho na variável `LOCAL_FOLDER`).

3. **Arquivo de Erros**:
   - O script salvará os nomes dos arquivos que falharam no upload em `./files_with_error.txt`. Você pode alterar o caminho na variável `FILES_WITH_ERROR_FOLDER`.

### 3. Instalação das Dependências

Instale a biblioteca `requests` se ainda não a tiver:

```bash
pip install requests
```

## 4. Execução e Resultados

### Como Executar o Script

1. **Preparação**:

   - Certifique-se de que os arquivos que deseja enviar estejam na pasta `./planilhas`.
   - Verifique se o endpoint da API (`UPLOAD_URL`) está configurado corretamente no script.

2. **Execução**:

   - Abra o terminal e navegue até o diretório onde o script está localizado.
   - Execute o script com o seguinte comando:
     ```bash
     python nome_do_arquivo.py
     ```
     Substitua `nome_do_arquivo.py` pelo nome do arquivo do script.

3. **Monitoramento**:

   - O script exibirá mensagens no terminal indicando o progresso do upload:
     ```
     Processando 'arquivo1.xlsx'...
     Arquivo 'arquivo1.xlsx' enviado com sucesso para a API.
     Processando 'arquivo2.xlsx'...
     Falha ao enviar 'arquivo2.xlsx'. Código de status: 500, Resposta: Internal Server Error
     ```

4. **Resultados**:

   - **Arquivos Enviados com Sucesso**: Para cada arquivo enviado com sucesso, você verá uma mensagem como:
     ```
     Arquivo 'arquivo1.xlsx' enviado com sucesso para a API.
     ```
   - **Arquivos com Erro**: Se algum arquivo falhar no upload, o nome do arquivo será salvo no arquivo `files_with_error.txt`. O script também exibirá uma mensagem de erro no terminal:
     ```
     Falha ao enviar 'arquivo2.xlsx'. Código de status: 500, Resposta: Internal Server Error
     ```

5. **Verificação do Arquivo de Erros**:

   - Após a execução, verifique o arquivo `files_with_error.txt` para ver quais arquivos falharam no upload. O conteúdo do arquivo será algo como:
     ```
     arquivo2.xlsx
     arquivo3.xlsx
     ```

6. **Conclusão**:
   - O script finalizará com uma mensagem indicando que os arquivos com erro foram salvos:
     ```
     Arquivos com erro salvos com sucesso em: ./files_with_error.txt
     ```
