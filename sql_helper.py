import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn

def create_table(conn, arg):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param arg: format of the table
    :return:
    """
    try:
        c = conn.cursor()
        stmt = "CREATE TABLE IF NOT EXISTS %s" % arg
        c.execute(stmt)
    except Error as e:
        print(e)

def create_monster(conn, monster):
    """
    Create a new monster into the Monsters table
    :param conn:
    :param monster:
    :return: monster name
    """
    try:
        cur = conn.cursor()
        stmt = '''INSERT INTO Monsters(name,Monster_id,Str,Dex,Con,Int,Wis,Cha,HP)
                VALUES(?,?,?,?,?,?,?,?,?)'''
        cur.execute(stmt, monster)
        conn.commit()
    except Error as e:
        print(e)
     

def monster_info(conn, monster):
    """
    read monster info from the Monsters table
    :param conn:
    :param monster:
    :return: monster info
    """
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        stmt = '''SELECT * FROM Monsters WHERE name=?'''
        cur.execute(stmt, (monster,))
        conn.commit()
        rows = cur.fetchall()
        info={}
        for row in rows:
            info.update(dict(row))
        return info
    except Error as e:
        print(e)

def monster_count(conn,Monster_id):
    """
    return number of same monster
    :param conn:
    :param Monster_id:
    :return: monster number
    """
    try:
        cur = conn.cursor()
        stmt = "SELECT COUNT(*) FROM Monsters WHERE Monster_id=?"
        cur.execute(stmt, (Monster_id,))
        conn.commit()
        return cur.fetchall()[0][0]
    except Error as e:
        print(e)


def update_monster(conn,name,column,new_value,table="Monsters"):
    """
    update monster info
    :param conn:
    :param name:
    :param column:
    :param new_value:
    :return: monster update log
    """
    try:
        cur = conn.cursor()
        ID = monster_info(conn,name)['ID']
        stmt = 'UPDATE {} SET {} = \'{}\' WHERE ID = {}'.format(table,column,new_value,ID)
        cur.execute(stmt)
        conn.commit()
        return "Updated successfully!"
    except Error as e:
        print(e)