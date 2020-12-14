# API по определению вероятности троллингового ответ на вопрос
## Что нужно для начала работы?
1) Зайти на web сервис ...,
2) Зарегистрироваться
3) В личном кабинете выбрать тариф и получить индивидуальный key_api
4) Воспользоваться API из файла `troll_api.py`</br>
*Ознакомиться с примером работы возможно [Здесь](https://drive.google.com/file/d/18gR1kZCtjQudnPTakeTFXOxGMRZzEKPO/view?usp=sharing)*
## Какие запросы возможно отправить через API?
1) Запрос на определение вероятности троллинга вопроса ответом
2) Запрос на определение вероятности троллинга для всех вопросов и ответов с требуемого портала (необходима ссылка на портал)
3) Запрос на интерпретацию результатов вероятности (таблица с главными вкладами признаков при определении вероятности конкретной пары вопрос-ответ)
## Какие посылать запросы через API?
Чтобы послать запрос необходимо объявить объект класса API и указать индивидуальный key_api
`from troll_api import FindTrollApi`</br>
`api = FindTrollApi(key_api="your_key_api")`</br>
### Запрос на определение вероятности троллинга вопроса ответом
В метод `api.get_proba()` передаются атрибуты `question` и `answer`, содержащие данные по вопросу и ответу.</br>
Атрибуты могут задаваться как строкой, так и списком строк (число запросов равно числу элементов списка).</br>
Атрибут `save_to_json` задаёт возможность сохранения ответа на запрос в json формате на вашем локальном компьютере.</br>
Примеры:
</br>
Отправится один запрос</br>
`api.get_proba(question = "Вопрос", answer = "Ответ")`</br>
</br>
Отправится два запроса с одинаковыми ответами на вопросы</br>
`api.get_proba(question = ["Вопрос1", "Вопрос2"], answer = "Ответ")`</br>
</br>
Отправится два запроса о ответами на однаковый вопрос</br>
`api.get_proba(question = "Вопрос", answer = ["Ответ1", "Ответ2"])`</br>
</br>
Отправится два запроса с ответами на соответствующие вопросы</br>
`api.get_proba(question = ["Вопрос1", "Вопрос2"], answer = ["Ответ1", "Ответ2"])`</br>
</br>
Узнать оставшееся число запросов возможно вызвав метод<br/>
`api.get_count_available_requests()`
### Запрос на определение вероятности троллинга по ссылке на портал
В метод `api.get_proba_from_link()` передаются атрибуты `link` и `type_parser`, содержащие данные по ссылке на интересуемый пост портала и тип парсера для чтения данных с портала.</br>
Параметром по умолчанию атрибута `type_parser` стоит `answers_mail.ru`, отвечающий за изъятие информации по ссылке на вопрос портала ["Ответы Mail.ru"](https://otvet.mail.ru/).</br>
Все доступные на данный момент парсеры возможно получить вызвав метод `api.get_available_type_parsers()`.</br>
Атрибут `save_to_json` задаёт возможность сохранения ответа на запрос в json формате на вашем локальном компьютере.</br>
Примеры:</br>
`api.get_proba(link = "https://otvet.mail.ru/question/3817867")`</br>
### Запрос на интерпретацию результатов вероятности
