import mysql.connector

def mark_attendance(student_name):
    try:
        # Establish a connection
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port='3306',
            database='student_attendance'
        )

        # Create a cursor object
        cursor = mydb.cursor()

        # Update attendance status
        update_query = "UPDATE student SET attendance = 'present' WHERE rollno = %s"
        cursor.execute(update_query, (student_name,))
        mydb.commit()

        # Close the cursor and connection
        cursor.close()
        mydb.close()

        print(f"Attendance marked as 'present' for {student_name}")
    except Exception as e:
        print(f"Error updating attendance: {e}")

# Define other functions or code as needed

# If this module is run directly, it won't execute the code below
if __name__ == "__main__":
    pass
