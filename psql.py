def return_first_last_names_mentors():
    os.system("clear")
    conn = initialize_database()
    cursor = conn.cursor()
    rows = cursor.execute(""" SELECT CONCAT_WS(' ', last_name, first_name) AS full_name FROM mentors """)
    rows = cursor.fetchall()
    title = "Mentors"
    ui.print_table(rows, title)


def return_miskolc_mentor_nicknames():
    os.system("clear")
    conn = initialize_database()
    cursor = conn.cursor()
    rows = cursor.execute(""" SELECT nick_name FROM mentors WHERE city = 'Miskolc' """)
    rows = cursor.fetchall()
    title = "Nicknames"
    ui.print_table(rows, title)


def carol_full_name():
    os.system("clear")
    conn = initialize_database()
    cursor = conn.cursor()
    rows = cursor.execute(""" SELECT CONCAT_WS(' ', first_name, last_name) AS full_name, phone_number
                              FROM applicants WHERE first_name = 'Carol' """)
    rows = cursor.fetchall()
    title = "Full name and phone number"
    ui.print_table(rows, title)