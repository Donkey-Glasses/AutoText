import sqlite3
import json


# def read_names():
#     with open("names.json") as f:
#         return json.load(f)


def setup():
    connection = sqlite3.connect('game_data.dat')
    cursor = connection.cursor()
    return connection, cursor


def cleanup(connection):
    connection.commit()
    connection.close()


if __name__ == "__main__":
    con, cur = setup()
    # cur.execute("DROP TABLE first_names")
    # con.commit()
    # cur.execute("DROP TABLE last_names")
    # con.commit()
    # cur.execute("""CREATE TABLE first_names (
    #             name text,
    #             species text,
    #             gender text
    #             )""")
    # con.commit()
    # cur.execute("""CREATE TABLE last_names (
    #             name text,
    #             species text)""")
    # con.commit()
    # names = read_names()
    # for key, val in names.items():
    #     split = key.split('-')
    #     if len(split) == 2:
    #         for name in val:
    #             cur.execute("INSERT INTO last_names VALUES (?, ?)", (name, split[0]))
    #     elif len(split) == 3:
    #         for name in val:
    #             cur.execute("INSERT INTO first_names VALUES (?, ?, ?)", (name, split[0], split[1]))
    #     con.commit()
    # # cur.execute("""UPDATE genders
    # #                SET objective = 'it'
    # #                WHERE gender='object'""")
    # cur.execute("SELECT * FROM first_names")
    # print(cur.fetchall())
    # cur.execute("SELECT * FROM last_names")
    # print(cur.fetchall())
    cleanup(con)
