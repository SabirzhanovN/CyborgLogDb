from django.db import connection


def check_count_of_data():
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM "shopApp_loggingmoves";
        """
    )

    data = cursor.fetchall()
    print(len(data))

    return len(data)


def clear_db():
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            TRUNCATE "shopApp_loggingmoves";
            """
        )

        connection.commit()

        return 0
    except Exception as ex:
        return str(ex)

