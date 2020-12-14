# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime
from time import time

class FindTrollApi:
    """API по определению вероятности троллингового ответ на вопрос

    """
    def __init__(self, key_api, url_to_server='http://127.0.0.1:5000', treshold=0.5):
        """

        Args:
            key_api (str): идентификационный ключ
            url_to_server (str): URL до главной страницы приложения. Defaults to 'http://127.0.0.1:5000'.
            treshold (float): порог отсечения троллинга по вероятности, при автоматической модерации. Defaults to 0.5.
        """
        self._headers = {
            'Content-type': 'application/json',
            'Accept': 'text/plain',
            'Content-Encoding': 'utf-8',
            }
        self._key_api = key_api
        self._url_to_server = url_to_server
        self._treshold = treshold
    
    def _save_to_json(self, response, path_to_save):
        """Сохранение данных полученного ответа в файл

        Args:
            response (dict): сохраняемые данные
            path_to_save (str): путь до сохраняемого файла
        """
        with open(path_to_save, "w", encoding="utf-8") as write_file:
            json.dump(response, write_file, indent=2, ensure_ascii=False)

    def set_treshold(self, treshold):
        """Метод для задания порога отсечения троллинга, при автоматической модерации

        Args:
            treshold (float): порога отсечения троллинга
        """
        self._treshold = treshold

    def get_count_available_requests(self,
                                     save_to_json=False, 
                                     path_to_save="available_requests_{}.json".format(datetime.today().strftime("%Y-%m-%d_%H.%M.%S")),
                                     timeout=300):
        """Метод для определения доступного количества запросов пользователя

        Args:
            save_to_json (bool): сохранение полученной информации в файл. Defaults to False.
            path_to_save (str): путь до сохраняемого файла. Defaults to "available_requests_{}.json".format(datetime.today().strftime("%Y-%m-%d_%H.%M.%S")).
            timeout (int): максимальное время ожидания ответа от сервера, сек. Defaults to 300.

        Returns:
            dict: параметры доступных запросов для пользователя
        """
        answer = requests.post(
            self._url_to_server + "/get_query_left", 
            data=json.dumps({"key_api":self._key_api}), 
            headers=self._headers,
        )
        response = answer.json()
        if save_to_json: self._save_to_json(response, path_to_save)
        return response
        
    def get_available_type_parsers(self,
                                    save_to_json=False, 
                                    path_to_save="available_parsers_{}.json".format(datetime.today().strftime("%Y-%m-%d_%H.%M.%S")),
                                    timeout=300):
        """Метод для определения доступного количества запросов пользователя

        Args:
            save_to_json (bool): сохранение полученной информации в файл. Defaults to False.
            path_to_save (str): путь до сохраняемого файла. Defaults to "available_parsers_{}.json".format(datetime.today().strftime("%Y-%m-%d_%H.%M.%S")).
            timeout (int): максимальное время ожидания ответа от сервера, сек. Defaults to 300.

        Returns:
            dict: параметры доступных типов парсеров для порталов
        """
        answer = requests.post(
            self._url_to_server + "/get_available_parsers", 
            data=json.dumps({"key_api":self._key_api}),
            headers=self._headers,
        )
        response = answer.json()
        if save_to_json: self._save_to_json(response, path_to_save)
        return response

    def get_proba(self, 
                  question,
                  answer, 
                  save_to_json=False, 
                  path_to_save="request_proba_{}.json".format(datetime.today().strftime("%Y-%m-%d_%H.%M.%S")),
                  timeout=300):
        """Формирование запроса на сервер и получение данных о вероятности троллинга при ответе на вопрос

        Args:
            question (str, list): [description]
            answer (str, list): [description]
            save_to_json (bool): сохранение полученной информации в файл. Defaults to False.
            path_to_save (str): путь до сохраняемого файла. Defaults to "request_proba_{}.json".format(datetime.today().strftime("%Y-%m-%d_%H.%M.%S")).
            timeout (int): максимальное время ожидания ответа от сервера, сек. Defaults to 300.

        Returns:
            dict: данные о вероятности троллинга при ответе на вопрос
        """
        answer = requests.post(
            self._url_to_server + "/get_proba", 
            data=json.dumps({
                "question":question,
                "answer":answer,
                "treshold":self._treshold,
                "key_api":self._key_api
            }), 
            headers=self._headers,
            timeout=timeout
        )
        response = answer.json()
        if save_to_json: self._save_to_json(response, path_to_save)
        return response

    def get_proba_from_link(self, 
                            link,
                            type_parser="answers_mail.ru", 
                            save_to_json=False, 
                            path_to_save="request_proba_from_link_{}.json".format(datetime.today().strftime("%Y-%m-%d_%H.%M.%S")),
                            timeout=300):
        """Формирование запроса на сервер и получение данных о вероятности троллинга при ответе на вопрос по сслыке на пост портала

        Args:
            link ([type]): ссылка на пост портала
            type_parser (str): выбор типа парсера для извлечения данных с поста портала. Defaults to "answers_mail.ru".
            save_to_json (bool): сохранение полученной информации в файл. Defaults to False.
            path_to_save (str): путь до сохраняемого файла. Defaults to "request_proba_from_link_{}.json".format(datetime.today().strftime("%Y-%m-%d_%H.%M.%S")).
            timeout (int): максимальное время ожидания ответа от сервера, сек. Defaults to 300.

        Returns:
            dict: данные о вероятности троллинга при ответе на вопрос
        """
        answer = requests.post(
            self._url_to_server + "/get_link", 
            data=json.dumps({
                "link":link,
                "parser":type_parser,
                "treshold":self._treshold,
                "key_api":self._key_api
            }), 
            headers=self._headers,
            timeout=timeout
        )
        response = answer.json()
        if save_to_json: self._save_to_json(response, path_to_save)
        return response

if __name__ == "__main__":
    api = FindTrollApi(key_api="qwerty")
    N = 7
    question = ["questionquestion"] * N
    answer = "answer"
    link = "1234567"
    t1 = time()
    data_ = api.get_proba(question, answer, save_to_json=True)
    print(time()-t1)
    """
    data1 = {
        "question":["questionquestion"]*N,
        "answer":"answer",
        "link":"1234567"
    }
    with open("path_to_save.json", "w", encoding="utf-8") as write_file:
                json.dump(data1, write_file, indent=2, ensure_ascii=False)
    """
