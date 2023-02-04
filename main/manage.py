from main.utils import get_response, get_html_tags, convert_to_tuple

def question_3():
    html = get_response("https://greenatom.ru/").text
    tags = get_html_tags(html)
    tags_with_attrs = list(filter(lambda item: item[1] != '', tags))

    return len(tags), len(tags_with_attrs)

def question_4():
    json = get_response("https://ifconfig.me/all.json/").json()
    return json["ip_addr"]

def question_5(v1: str, v2: str):
    A, B = convert_to_tuple(v1, v2)

    if A == B:
        return 0
    elif A < B:
        return -1

    return 1


if __name__ == "__main__":
    print(question_3())
    print(question_4())
    print(question_5("1.1.12.0", "1.1.12."))