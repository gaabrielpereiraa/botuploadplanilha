import os
import requests

# Endpoint da API para upload de arquivos
UPLOAD_URL = "http://localhost:3000/questao/upload" 

# Pasta local que contém os arquivos
LOCAL_FOLDER = "./planilhas"
FILES_WITH_ERROR_FOLDER = "./files_with_error.txt"  # Arquivo para salvar os nomes dos arquivos com erro

# Lista para armazenar os nomes dos arquivos que tiveram erro durante o upload
files_with_error = []

def upload_file_to_api(file_name, file_path):
    """Faz o upload de um arquivo e seu nome para a API usando uma requisição POST."""
    try:
        with open(file_path, 'rb') as file:
            # Prepara o payload para a requisição POST
            files = {
                'file': (file_name, file)  # 'file' é o objeto do arquivo
            }
            data = {
                'name': file_name  # 'name' é o nome do arquivo
            }
            # Envia a requisição POST
            response = requests.post(UPLOAD_URL, files=files, data=data)
            
            # Verifica a resposta
            if response.status_code == 201:
                print(f"Arquivo '{file_name}' enviado com sucesso para a API.")
            else:
                print(f"Falha ao enviar '{file_name}'. Código de status: {response.status_code}, Resposta: {response.text}")
                files_with_error.append(file_name)  # Adiciona o nome do arquivo à lista de erros
    except Exception as e:
        print(f"Erro ao enviar '{file_name}': {e}")

def main():
    # Verifica se a pasta local existe
    if not os.path.exists(LOCAL_FOLDER):
        print(f"A pasta '{LOCAL_FOLDER}' não existe.")
        return

    # Itera por todos os arquivos na pasta local
    for file_name in os.listdir(LOCAL_FOLDER):
        file_path = os.path.join(LOCAL_FOLDER, file_name)
        
        # Verifica se é um arquivo (não um diretório)
        if os.path.isfile(file_path):
            print(f"Processando '{file_name}'...")
            
            # Faz o upload do arquivo e seu nome para a API
            upload_file_to_api(file_name, file_path)
        else:
            print(f"Ignorando '{file_name}' (não é um arquivo).")

    # Salva os nomes dos arquivos que tiveram erro em um arquivo de texto
    with open(FILES_WITH_ERROR_FOLDER, 'w') as file:
        for line in files_with_error:
            file.write(line + '\n')
    print(f"Arquivos com erro salvos com sucesso em: {FILES_WITH_ERROR_FOLDER}")

if __name__ == '__main__':
    main()