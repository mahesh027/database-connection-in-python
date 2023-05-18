import sqlite3
con=sqlite3.connect('users.db')

def insertData(name,age,city):  #id variable not included as it is in autoincremental mode
    qry="insert into users (NAME,AGE,CITY) values (?,?,?)"
    con.execute(qry,(name,age,city))
    con.commit()
    print("user details added")

print("""
1.Insert
2.Update
3.Delete
4.Select
""")
ch=1
while ch==1 :
    c=int(input("select your choice"))
    if(c==1):
       print("Add new Record")
       name=input("enter the name")
       age=int(input("enter age"))
       city=input("enter the city")
    elif(c==2):
       print("edit a record")
    elif(c==3):
       print("Delete a record")
    elif(c==4):
       print("print all record")
    else:
       print("invalid selection")
    ch=int(input("Enter 1 to continue"))
print("exited")
    
