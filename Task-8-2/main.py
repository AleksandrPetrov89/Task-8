import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """ Создает на Яндекс.Диске папку "Test" и загружает в нее указанный файл

            file_path - название файла, который нужно загрузить на Яндекс.Диск
        """
        path_to_folder = 'Test'
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': self.token}
        params = {'path': path_to_folder}
        requests.put(url, params=params, headers=headers)

        path = f'{path_to_folder}/{file_path}'
        params = {'path': path, 'overwrite': 'true'}
        url += '/upload'
        resp = requests.get(url, params=params, headers=headers)
        data = resp.json()

        url = data['href']
        with open(file_path, 'rb') as f:
            requests.put(url, files={"file": f})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = ''
    uploader = YaUploader(token)
    path_to_file = 'Task-8-2.txt'
    uploader.upload(path_to_file)
    path_to_file = 'Горы.jpg'
    uploader.upload(path_to_file)
