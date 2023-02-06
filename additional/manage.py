from main.db import init_db, close_session
from main.views import create_content_view
from main.utils import check_db_connect


if __name__ == "__main__":
    # No comments about this...
    # But fck.. (docker-compose) healthcheck not worked.
    check_db_connect()

    init_db()
    create_content_view()
    close_session()

    print("Complete Insertions.")