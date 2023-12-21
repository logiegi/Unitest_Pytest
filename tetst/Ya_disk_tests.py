from unittest import TestCase

from data.Ya_disc_folder import *


class YaTest(TestCase):
    def setUp(self) -> None:
        self.yandex_token = 'Токен яндекса'
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers_folder = {"Authorization": f"OAuth {self.yandex_token}"}
        self.folder_name = "Название папки"
        self.params_folder = {"path": f"/{self.folder_name}"}

    def test_folder(self):
        res = 201
        expected = YaDiskCheck.create_folder(self)
        self.assertEqual(res, expected)

    def test_200(self):
        res = 200
        expected = YaDiskCheck.cod_answer(self)
        self.assertEqual(res, expected)
