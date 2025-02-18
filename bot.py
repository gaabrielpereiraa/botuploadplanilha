import os
import requests

# API endpoint for uploading files
UPLOAD_URL = "http://localhost:3000/questao/upload"  # Replace with your API endpoint

# Local folder containing the files
LOCAL_FOLDER = "./planilhas"  # Replace with the path to your local folder

def upload_file_to_api(file_name, file_path):
    """Upload a file and its name to the API using a POST request."""
    try:
        with open(file_path, 'rb') as file:
            # Prepare the payload for the POST request
            files = {
                'file': (file_name, file)  # 'file' is the file object
            }
            data = {
                'name': file_name  # 'name' is the name of the file
            }
            # Send the POST request
            response = requests.post(UPLOAD_URL, files=files, data=data)
            
            # Check the response
            if response.status_code == 200:
                print(f"Successfully uploaded '{file_name}' to the API.")
            else:
                print(f"Failed to upload '{file_name}'. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error uploading '{file_name}': {e}")

def main():
    # Check if the local folder exists
    if not os.path.exists(LOCAL_FOLDER):
        print(f"The folder '{LOCAL_FOLDER}' does not exist.")
        return

    # Iterate through all files in the local folder
    for file_name in os.listdir(LOCAL_FOLDER):
        file_path = os.path.join(LOCAL_FOLDER, file_name)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            print(f"Processing '{file_name}'...")
            
            # Upload the file and its name to the API
            upload_file_to_api(file_name, file_path)
        else:
            print(f"Skipping '{file_name}' (not a file).")

if __name__ == '__main__':
    main()