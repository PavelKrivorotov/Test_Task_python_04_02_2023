from main.db import init_db, close_session
from main.views import create_content_view


if __name__ == "__main__":
    init_db()
    create_content_view()
    close_session()

    print("Complete Insertions.")