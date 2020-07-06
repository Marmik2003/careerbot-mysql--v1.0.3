import mysql.connector as mscon
from random import choice

cbdb = mscon.connect(host="localhost", user="careerbot", passwd="1234", database="careerbot_response")
cbcur = cbdb.cursor()


def chat_reply(ui_lower):
    response='"'+ui_lower+'"'
    sql = "SELECT output FROM res_table WHERE INPUT=%s"%response
    cbcur.execute(sql)
    cbres = cbcur.fetchall()
    resstr = ()
    for row in cbres:
        resstr += row
    i = choice(resstr)
    final=""
    for o in i:
        final += o
    return final

