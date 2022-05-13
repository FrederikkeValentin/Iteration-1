class MySQL_connector:
    """Dette er en class for connecter fra MySQL til Python"""

def check_kodeord(username, pw):
    connection = get_connection()
    mycursor = connection.cursor()
    if not check_username(username):
        return (False, "No user found", 0, 0)
    query = ("SELECT password, usertypeid, id FROM users where username = %s")
    mycursor.execute(query, (username,))
    this_password = ""
    this_usertypeid = 0
    this_userid = 0
    for (password) in mycursor:
        this_password = password[0]
        this_usertypeid = password[1]
        this_userid = password[2]
    mycursor.close()
    connection.close()
    if pw == this_password:
        return (True, "Success", this_usertypeid, this_userid)
    else:
        return (False, "Wrong password", 0, 0)