import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="test"
)

cursor = mydb.cursor()

def checkTableExists(dbCursor, tablename):
    dbcur = dbCursor
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        return True
    return False

if(not checkTableExists(cursor, "GitUser")):
    cursor.execute("CREATE TABLE GitUser (name VARCHAR(255), email VARCHAR(255), company VARCHAR(255), id VARCHAR(255), PRIMARY KEY (id))")
if(not checkTableExists(cursor, "FreshdeskContact")):
    cursor.execute("CREATE TABLE FreshdeskContact (name VARCHAR(255), email VARCHAR(255), avatar TEXT, id int(11) NOT NULL auto_increment, jobTitle VARCHAR(255), tags TEXT, PRIMARY KEY (id))")
if(not checkTableExists(cursor, "CreatedAccountLink")):
    cursor.execute("CREATE TABLE CreatedAccountLink (id int(11) NOT NULL auto_increment, gitUserId VARCHAR(255),  frashdeskUserId int(11), PRIMARY KEY (id), FOREIGN KEY(gitUserId) REFERENCES GitUser (id), FOREIGN KEY (frashdeskUserId) REFERENCES FreshdeskContact (id))")
cursor.close()