import pytest
import requests


class TestPodcast:
    texts_search_thematic_matching = [
        "включи подкаст про психологию"
        "включи подкаст про спорт",
        "включи подкаст про искусство"
    ]

    @pytest.mark.parametrize("text", texts_search_thematic_matching)
    def test_search_thematic_matching(self, text):
        url = "https://vc1.go.mail.ru/phrase/create/text"
        data = {"session_id": "f41fe49a-393d-4e56-b1d4-4e23b21e0958",
                "device_id": ":c:m:android:23fc82a4e6c146b7a2730bba66924358",
                "skillserver_type": "skillteam",
                "text": text}
        response = requests.post(url, params=data)
        print(response.status_code)
        parced_response_text = response.json()
        get_intent = parced_response_text['result']['phrase_result']['intent']
        print(get_intent)
        assert get_intent == "podcasts_v2.search_thematic"

    def test_discover_matching(self):
        url = "https://vc1.go.mail.ru/phrase/create/text"
        data = {"session_id": "f41fe49a-393d-4e56-b1d4-4e23b21e0958",
                "device_id": ":c:m:android:23fc82a4e6c146b7a2730bba66924358",
                "skillserver_type": "skillteam",
                "text": "какие подкасты у тебя есть"}
        response = requests.post(url, params=data)
        print(response.status_code)
        parced_response_text = response.json()
        get_intent = parced_response_text['result']['phrase_result']['intent']
        print(get_intent)
        assert get_intent == "podcasts_v2.discover"

    def test_discover_choice(self):
        text = ""  # просто пустая переменная, чтоб начать цикл
        try_count = 0  # эта штука нужна, чтоб цикл не был вечным, сначала он был вечным
        expexted_count = 4  # тоже
        url = "https://vc1.go.mail.ru/phrase/create/text"
        data = {"session_id": "f41fe49a-393d-4e56-b1d4-4e23b21e0958",
                "device_id": ":c:m:android:23fc82a4e6c146b7a2730bba66924358",
                "skillserver_type": "skillteam",
                "text": "какие подкасты у тебя есть"}
        while text.find("политику") == -1 and try_count <= expexted_count:  # пока в выдаче не попадется политику
            # спрашиваем снова эту тему
            response = requests.post(url, params=data)
            parced_response_text = response.json()
            text = parced_response_text['result']['phrase_result']['commands'][0]['text']  # выбор сначала по ключу,
            # а потом по индексу из поиска
            try_count = try_count + 1
        assert try_count <= expexted_count, f"За {expexted_count} попыток не попалась тема политика"
        data = {"session_id": "f41fe49a-393d-4e56-b1d4-4e23b21e0958",
                "device_id": ":c:m:android:23fc82a4e6c146b7a2730bba66924358",
                "skillserver_type": "skillteam",
                "text": "политика"}
        response = requests.post(url, params=data)  # теперь уже выбираем тему "политика из предложенных"
        parced_response_text1 = response.json()
        text = parced_response_text1['result']['phrase_result']['commands'][0]['text']
        assert text.find("Слушаем подкаст") != -1  # оказалось, что -1 это не нашлось, то есть тут проверка отрицания,
        # что ничего не нашлось
