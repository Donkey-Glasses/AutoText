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
    # cur.execute("SELECT species FROM species")
    # con.commit()
    # x = cur.fetchall()
    # for y in x:
    #     print(y)
    # print(type(x))
    # cur.execute("DROP TABLE professions")
    # con.commit()
    # cur.execute("""ALTER TABLE professions
    #                RENAME COLUMN professions TO profession""")
    # cur.execute("")
    # con.commit()
    # cur.execute("""CREATE TABLE professions (
    #             name text,
    #             plural text,
    #             strength int,
    #             agility int,
    #             constitution int,
    #             intelligence int,
    #             wits int,
    #             willpower int
    #             )""")
    # con.commit()
    # cur.execute("INSERT INTO professions VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('warrior', 'warriors', 4, 2, 4, 0, 2, 2))
    # cur.execute("INSERT INTO professions VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('rogue', 'rogues', 2, 4, 0, 2, 4, 2))
    # cur.execute("INSERT INTO professions VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('mage', 'mages', 0, 2, 2, 4, 2, 4))
    # cur.execute("INSERT INTO professions VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('priest', 'priests', 2, 2, 2, 4, 0, 4))
    # cur.execute("INSERT INTO professions VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    #             ('skirmisher', 'skirmisher', 0, 2, 0, -2, 2, -2))
    # con.commit()
    cur.execute("SELECT gender, weight FROM genders")
    x = cur.fetchall()
    print(x)
    for y in x:
        print(y)
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
