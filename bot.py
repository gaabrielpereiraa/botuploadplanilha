import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Endpoint da API para upload de arquivos
UPLOAD_URL = "http://localhost:3000/questao/upload" 

# Pasta local que contém os arquivos
LOCAL_FOLDER = "./planilhas"
FILES_WITH_ERROR_FOLDER = "./files_with_error.txt"  # Arquivo para salvar os nomes dos arquivos com erro

MAX_THREADS = 4

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
    # Check if the local folder exists
    if not os.path.exists(LOCAL_FOLDER):
        print(f"The folder '{LOCAL_FOLDER}' does not exist.")
        return

    # Get a list of all files in the local folder
    files_to_upload = [
        (file_name, os.path.join(LOCAL_FOLDER, file_name))
        for file_name in os.listdir(LOCAL_FOLDER)
        if os.path.isfile(os.path.join(LOCAL_FOLDER, file_name))
    ]

    if not files_to_upload:
        print("No files found in the folder.")
        return

    # Use ThreadPoolExecutor to upload files concurrently
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        # Submit upload tasks to the thread pool
        futures = [
            executor.submit(upload_file_to_api, file_name, file_path)
            for file_name, file_path in files_to_upload
        ]

        # Wait for all tasks to complete and handle results
        for future in as_completed(futures):
            try:
                future.result()  # This will raise any exceptions that occurred during the upload
            except Exception as e:
                print(f"An error occurred during upload: {e}")
    with open(FILES_WITH_ERROR_FOLDER, 'w') as file:
        for line in files_with_error:
            file.write(line + '\n')
    print(f"Arquivos com erro salvos com sucesso em: {FILES_WITH_ERROR_FOLDER}")

if __name__ == '__main__':
    main()