from main.utils import get_response, get_html_tags, convert_to_tuple


"""
    question1:
        В зависимости от того на какой позиции я нахожусь - ответы быут разные:
            Если же на backend:
                1) Просмотреть лог ошибок в поисках данного 5ХХ кода.
                2) Если данная проблема подтвердится - сообщить ребятам постарше))
                3) Если же я одинокий владелец и разработчик (что прискорбно), то
                   устранять данную проблему)).

    question2:
    ```python
        from typing import Callable, Any

        def create_handlers(callback: Callable[[int], Any]) -> list[Callable[[None], Any]]:
            handlers: list[Callable[[None], Any]] = []
            for step in range(5):
                handlers.append(lambda: callback(step))
            return handlers

        def execute_handlers(handlers: list[Callable[[None], Any]]) -> None:
            for handler in handlers:
                handler()
    ```
"""

def question_3():
    html = get_response("https://greenatom.ru/").text
    tags = get_html_tags(html)
    tags_with_attrs = list(filter(lambda item: item[1] != '', tags))

    ans = f"All tags {len(tags)}. Tags with attrs {len(tags_with_attrs)}"
    print(ans)

    return len(tags), len(tags_with_attrs)

def question_4():
    json = get_response("https://ifconfig.me/all.json/").json()

    ans = f"Youre ip is {json['ip_addr']}"
    print(ans)

    return json["ip_addr"]

def question_5(v1: str, v2: str):
    A, B = convert_to_tuple(v1, v2)

    if A == B:
        print(f"{v1} == {v2}")
        return 0
    elif A < B:
        print(f"{v1} < {v2}")
        return -1

    print(f"{v1} > {v2}")
    return 1


if __name__ == "__main__":
    question_3()
    question_4()
    question_5("1.1.12.0", "1.1.12.")