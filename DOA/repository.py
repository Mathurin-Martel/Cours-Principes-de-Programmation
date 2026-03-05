from db import get_connection
def get_all_students():
    conn=get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * from students")
    result=cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def get_student_by_id(student_id):
    conn=get_connection()
    cursor = conn.cursor(dictionary=True)

    query="SELECT * from students WHERE id=%s"
    cursor.execute(query,student_id)
    #%s pour éviter l'injection SQL
    result=cursor.fetchone()

    cursor.close()
    conn.close()

    return result
