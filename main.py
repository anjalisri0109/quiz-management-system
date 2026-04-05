import mysql.connector as msq

# ---------------- EASY ---------------- #

def display_easy():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()
    cur.execute('select * from Easy;')
    data = cur.fetchall()
    for i in data:
        print(i)
    mycon.close()

def add_easy():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()
    t = input('ENTER THE TOPIC: ').upper()
    s = input('ENTER QUESTION: ')
    o = input('ENTER OPTIONS: ')
    c = input('ENTER CORRECT ANSWER: ')
    tr = input('ENTER TRIVIA: ')

    q = "INSERT INTO Easy VALUES (%s,%s,%s,%s,%s)"
    cur.execute(q, (t, s, o, c, tr))

    mycon.commit()
    mycon.close()
    print("QUESTION ADDED SUCCESSFULLY")

def remove_easy():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()
    t = input('ENTER THE TOPIC: ').upper()
    s = input('ENTER QUESTION: ')

    q = "DELETE FROM Easy WHERE topic=%s AND ques=%s"
    cur.execute(q, (t, s))

    mycon.commit()
    mycon.close()
    print("QUESTION REMOVED")

def ans_easy():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()
    t = input('ENTER THE TOPIC: ').upper()

    cur.execute('select * from Easy;')
    data = cur.fetchall()
    m = 0

    for i in data:
        if t == i[0]:
            print(i[1])
            print("\n")
            print(i[2])
            print("\n")

            c = input('ENTER THE ANSWER: ')
            if c == i[3]:
                print('CORRECT ANSWER!')
                m += 10
                print(i[4])
            else:
                print("HARD LUCK...")

            a = input("Press Y to continue, N to exit: ")
            if a.lower() == 'n':
                break

    print('YOUR SCORE IS', m)
    print('*' * 100)

# ---------------- MEDIUM ---------------- #

def display_medium():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()
    cur.execute('select * from Medium;')
    data = cur.fetchall()
    for i in data:
        print(i)
    mycon.close()

def add_medium():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()

    t = input('ENTER THE TOPIC: ').upper()
    s = input('ENTER QUESTION: ')
    o = input('ENTER OPTIONS: ')
    c = input('ENTER CORRECT ANSWER: ')
    tr = input('ENTER TRIVIA: ')

    q = "INSERT INTO Medium VALUES (%s,%s,%s,%s,%s)"
    cur.execute(q, (t, s, o, c, tr))

    mycon.commit()
    mycon.close()
    print("QUESTION ADDED SUCCESSFULLY")

def remove_medium():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()

    t = input('ENTER THE TOPIC: ')
    s = input('ENTER QUESTION: ')

    q = "DELETE FROM Medium WHERE topic=%s AND ques=%s"
    cur.execute(q, (t, s))

    mycon.commit()
    mycon.close()

def ans_medium():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()

    t = input('ENTER THE TOPIC: ').upper()
    cur.execute('select * from Medium;')
    data = cur.fetchall()
    m = 0

    for i in data:
        if t == i[0]:
            print(i[1])
            print("\n")
            print(i[2])
            print("\n")

            c = input('ENTER THE ANSWER: ')
            if c == i[3]:
                print('CORRECT ANSWER!')
                m += 10
                print(i[4])
            else:
                print("HARD LUCK...")

            a = input("Press Y to continue, N to exit: ")
            if a.lower() == 'n':
                break

    print('YOUR SCORE IS', m)
    print('*' * 100)

# ---------------- HARD ---------------- #

def display_hard():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()
    cur.execute('select * from Hard;')
    data = cur.fetchall()
    for i in data:
        print(i)
    mycon.close()

def add_hard():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()

    t = input('ENTER THE TOPIC: ').upper()
    s = input('ENTER QUESTION: ')
    o = input('ENTER OPTIONS: ')
    c = input('ENTER CORRECT ANSWER: ')
    tr = input('ENTER TRIVIA: ')

    q = "INSERT INTO Hard VALUES (%s,%s,%s,%s,%s)"
    cur.execute(q, (t, s, o, c, tr))

    mycon.commit()
    mycon.close()
    print("QUESTION ADDED SUCCESSFULLY")

def remove_hard():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()

    t = input('ENTER THE TOPIC: ')
    s = input('ENTER QUESTION: ')

    q = "DELETE FROM Hard WHERE topic=%s AND ques=%s"
    cur.execute(q, (t, s))

    mycon.commit()
    mycon.close()

def ans_hard():
    mycon = msq.connect(host="localhost", user="root", password="", database="12A123")
    cur = mycon.cursor()

    t = input('ENTER THE TOPIC: ').upper()
    cur.execute('select * from Hard;')
    data = cur.fetchall()
    m = 0

    for i in data:
        if t == i[0]:
            print(i[1])
            print("\n")
            print(i[2])
            print("\n")

            c = input('ENTER THE ANSWER: ')
            if c == i[3]:
                print('CORRECT ANSWER!')
                m += 10
                print(i[4])
            else:
                print("HARD LUCK...")

            a = input("Press Y to continue, N to exit: ")
            if a.lower() == 'n':
                break

    print('YOUR SCORE IS', m)
    print('*' * 100)

# ---------------- MENU ---------------- #

print("\nWELCOME TO THE QUIZ\n")

ans = input("ENTER P FOR PLAYER / A FOR ADMIN: ")
l = input("ENTER LEVEL (E/M/H): ")

if l.lower() == 'e':
    if ans.lower() == 'a':
        display_easy()
    else:
        ans_easy()

elif l.lower() == 'm':
    if ans.lower() == 'a':
        display_medium()
    else:
        ans_medium()

elif l.lower() == 'h':
    if ans.lower() == 'a':
        display_hard()
    else:
        ans_hard()

else:
    print("INVALID CHOICE")