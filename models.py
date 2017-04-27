import sqlite3 as sql


class User:

    # Add a user to the db
    def add_user(nome, username, password, id=None):
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO utilizadores (id, nome, username, password) VALUES (?,?,?,?)", (id, nome, username, password))
        con.commit()
        con.close()

    # Remove user from the db
    def remove_user(id):
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute("DELETE FROM utilizadores WHERE id=?", (id))
        con.commit()
        con.close()

    # Get all users from the database
    def show_all_users():
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM utilizadores")
        users = cur.fetchall()
        con.close()
        return users

    # Delete all users
    def remove_all_users():
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute("DELETE * FROM utilizadores")
        con.commit()
        con.close()

    # Update user password
    def update_user(id, passwd):
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute("UPDATE utilizadores SET password=? WHERE id=?", (passwd, id))
        con.commit()
        con.close()


class Band:

    def add_band():
        pass

    def remove_band():
        pass

    def show_all_bands():
        pass

    def remove_all_bands():
        pass


class Album:

    def add_album():
        pass

    def remove_album():
        pass

    def show_all_album():
        pass

    def remove_all_album():
        pass

    def update_album():
        pass
