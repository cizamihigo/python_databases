import sqlite3
from bottle import route, run, debug, template

@route('/dnb')
def todo_liist():
    conn = sqlite3.connect('activityschedule.db')
    c = conn.cursor()
    c.execute("SELECT ID, ACTIVITY FROM todo WHERE STATUS LIKE '1'")
    output = c.fetchall()
    c.close()
    result = template('make_table', rows = output)
    return result
debug(True)
run(port = 1342, reloader= True)
