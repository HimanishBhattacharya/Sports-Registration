import mysql.connector
mysql=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="databasex"
)

mycursor=mysql.cursor()

def insert(name,email,phone,club):
    mycursor.execute("Insert into sportsclub values(NULL,%s,%s,%s,%s)",(name,email,phone,club))
    mysql.commit()


def football_members():
    mycursor.execute("Select id,Name,phone from sportsclub where club='Football Club'")
    listft=mycursor.fetchall()
    mysql.commit()
    return listft

def volleyball_members():
    mycursor.execute("Select id,Name,phone from sportsclub where club='Volleyball Club'")
    listft=mycursor.fetchall()
    mysql.commit()
    return listft

def Basketball_members():
    mycursor.execute("Select ID,Name,phone from sportsclub where club='Basketball Club'")
    listft=mycursor.fetchall()
    mysql.commit()
    return listft

def Cricket_members():
    mycursor.execute("Select id,name,phone from sportsclub where club='Cricket Club'")
    listft=mycursor.fetchall()
    mysql.commit()
    return listft

def tt_members():
    mycursor.execute("Select id,name,phone from sportsclub where club='Table Tennis Club'")
    listft=mycursor.fetchall()
    mysql.commit()
    return listft

def pubg_members():
    mycursor.execute("Select id,name,phone from sportsclub where club='PUBG Club'")
    listft=mycursor.fetchall()
    mysql.commit()
    return listft

