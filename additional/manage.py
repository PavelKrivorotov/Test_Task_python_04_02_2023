from main.db import init_db
from main.views import create_content_view


if __name__ == "__main__":
    init_db()
    create_content_view()