import sqlite3
import json


def read_characters():
    with open("characters.data") as chars:
        data = json.load(chars)
    return data["Gender"]


def setup():
    connection = sqlite3.connect('game_data.dat')
    cursor = connection.cursor()
    return connection, cursor


def cleanup(connection):
    connection.commit()
    connection.close()


if __name__ == "__main__":
    con, cur = setup()
    cur.execute("SELECT * FROM genders")
    # cur.execute("""UPDATE genders
    #                SET objective = 'it'
    #                WHERE gender='object'""")
    print(cur.fetchall())
    cleanup(con)
