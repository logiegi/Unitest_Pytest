import requests


class YaDiskCheck:
    def __init__(self, token_ya, urls, name_of_folder, folder_headers, folder_params):
        self.ya_token = token_ya
        self.folder_name = name_of_folder
        self.headers_folder = folder_headers
        self.params_folder = folder_params
        self.url = urls

    def cod_answer(self):
        response_folder = requests.get(self.url, headers=self.headers_folder, params=self.params_folder)
        return response_folder.status_code

    def create_folder(self):
        response_folder = requests.put(self.url, headers=self.headers_folder, params=self.params_folder)
        if response_folder.status_code != 201:
            requests.delete(self.url, headers=self.headers_folder, params=self.params_folder)
            response_folder = requests.put(self.url, headers=self.headers_folder, params=self.params_folder)
            return response_folder.status_code
        else:
            return response_folder.status_code
