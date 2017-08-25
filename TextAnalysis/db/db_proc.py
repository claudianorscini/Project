_db_path = "./db/db_trump.sqlite"
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_data(table, option = None):
    query = """
        SELECT
            *
        FROM
            {}
        {}
    """.format(table, option)

    conn = sqlite3.connect(_db_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute(query)

    return cur.fetchall()



def save_raw_text( document_id, title, body ):
    conn = sqlite3.connect(_db_path)
    cur = conn.cursor()
    cur.execute("""
        UPDATE document
        SET
            TITLE = ?,
            raw_text = ?
        WHERE
            id = ?
        """,
        (title, body, document_id)
    )
    conn.commit()

    return True


def delete_data_from_table( tab_name ):
    # given document id delete the record
    # delete from word_count where document_id = document_id
    conn = sqlite3.connect(_db_path)
    cur = conn.cursor()
    cur.execute(
        " DELETE FROM " + tab_name)
    conn.commit()

    return True


def insert_term_freq( document_id, term_freq, term_freq_norm):
    # given dictionary insert into the database
    # insert into word_count ( document_id, term, count ) VALUES ( document_id, key, value )
    conn = sqlite3.connect(_db_path)
    cur = conn.cursor()

    for key in term_freq.keys():
        cur.execute("""
            INSERT INTO wordcount
                (document_id, word, frequency, frequencynorm)
            VALUES
                (?, ?, ?, ?)
            """,
            (document_id, key, term_freq[key], term_freq_norm[key])
        )

    conn.commit()

    return True



def insert_totwordcount( tot_term_freq , doc_freq, tfidf ):
    # given dictionary insert into the database
    # insert into word_count ( document_id, term, count ) VALUES ( document_id, key, value )
    conn = sqlite3.connect(_db_path)
    cur = conn.cursor()

    for key in tot_term_freq.keys():
        cur.execute("""
            INSERT INTO totwordcount
                ( word, tottf, df, tfidf)
            VALUES
                (?, ?, ?, ?)
            """,
            ( key, tot_term_freq[key], doc_freq[key], tfidf[key])
        )

    conn.commit()

    return True
