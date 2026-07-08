import psycopg2
from config import DB_CONFIG


def get_db_connection():
    """
    Create and return a PostgreSQL connection.
    """
    return psycopg2.connect(**DB_CONFIG)


def insert_url(original_url):
    """
    Insert a new URL and return the generated ID.
    """

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO urls (original_url)
        VALUES (%s)
        RETURNING id;
    """

    cursor.execute(query, (original_url,))
    url_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return url_id


def update_short_code(url_id, short_code):
    """
    Update the short code for a URL.
    """

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        UPDATE urls
        SET short_code = %s
        WHERE id = %s;
    """

    cursor.execute(query, (short_code, url_id))

    connection.commit()

    cursor.close()
    connection.close()


def get_url_by_short_code(short_code):
    """
    Return the original URL corresponding to the short code.
    """

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        SELECT original_url
        FROM urls
        WHERE short_code = %s;
    """

    cursor.execute(query, (short_code,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return result[0]

    return None


def increment_click_count(short_code):
    """
    Increase click count by 1.
    """

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        UPDATE urls
        SET click_count = click_count + 1
        WHERE short_code = %s;
    """

    cursor.execute(query, (short_code,))

    connection.commit()

    cursor.close()
    connection.close()


def get_statistics(short_code):
    """
    Return complete statistics of a shortened URL.
    """

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            id,
            original_url,
            short_code,
            click_count,
            created_at
        FROM urls
        WHERE short_code = %s;
    """

    cursor.execute(query, (short_code,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result
