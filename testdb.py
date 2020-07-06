import mysql.connector as mscon
cbdb = mscon.connect(host="localhost", user="careerbot", passwd="1234", database="careerbot_response")
cbcur = cbdb.cursor()
cbcur.execute("SELECT * FROM res_table")
myres = cbcur.fetchall()
print(myres)