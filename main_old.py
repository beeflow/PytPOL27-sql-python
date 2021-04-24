import mysql.connector

dbconfig = {
    "host": "localhost",
    "user": "user",
    "password": "password",
    "database": "container_db"
}


class UseDatabase:
    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> "cursor":
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, *args, **kwargs) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


def main():
    with UseDatabase(dbconfig) as cursor:
        _SQL = "insert into book(book_title, book_isbn) values (%s, %s)"
        cursor.execute(_SQL, ("TDD", "64fewf84"))


if __name__ == '__main__':
    main()

