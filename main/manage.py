from main.utils import get_response, get_html_tags, convert_to_list


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

def mycmp(v1: str, v2: str):
    A = convert_to_list(v1)
    B = convert_to_list(v2)

    if A == B:
        print(f"{v1} == {v2}")
        return 0
    elif A < B:
        print(f"{v1} < {v2}")
        return -1

    print(f"{v1} > {v2}")
    return 1


if __name__ == "__main__":
    # question_3()
    # question_4()
    mycmp("1.1.12.0.0", "1.1.12")

    assert mycmp('1', '2') == -1
    assert mycmp('2', '1') == 1
    assert mycmp('1', '1') == 0
    assert mycmp('1.0', '1') == 0
    assert mycmp('1', '1.000') == 0
    assert mycmp('12.01', '12.1') == 0
    assert mycmp('13.0.1', '13.00.02') == -1
    assert mycmp('1.1.1.1', '1.1.1.1') == 0
    assert mycmp('1.1.1.2', '1.1.1.1') == 1
    assert mycmp('1.1.3', '1.1.3.000') == 0
    assert mycmp('3.1.1.0', '3.1.2.10') == -1
    assert mycmp('1.1', '1.10') == -1
    assert mycmp("0.1", "1.1") == -1
    assert mycmp("1.0.1", "1") == 1
    assert mycmp("7.5.2.4", "7.5.3") == -1
    assert mycmp("1.01", "1.001") == 0
    assert mycmp("1.0", "1.0.0") == 0
    assert mycmp("2", "2.0.0") == 0
    assert mycmp("1.01", "1.101") == -1