В /main находится осовная часть.
  Запускается:
    cd ../main
    python3 manage.py

В /additional находится дополнительная часть.
  Запускается:
    cd ../additional
    docker compose up

  К базе данных в контейнере можно подключиться:
    PGPASSWORD=postgres psql -h 0.0.0.0 -p 5432
