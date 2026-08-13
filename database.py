import sqlite3
import csv


# --------------------------------
# Database Connection
# --------------------------------

conn = sqlite3.connect("bmi.db")
cursor = conn.cursor()


# --------------------------------
# Create BMI Records Table
# --------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS bmi_records (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    weight REAL NOT NULL,

    height REAL NOT NULL,

    bmi REAL NOT NULL,

    category TEXT NOT NULL,

    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")


# --------------------------------
# Create User Profile Table
# --------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_profile (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    age INTEGER,

    gender TEXT,

    email TEXT,

    phone TEXT

)
""")


conn.commit()



# =================================
# BMI RECORD FUNCTIONS
# =================================


def save_record(name, weight, height, bmi, category):

    try:

        cursor.execute("""
        INSERT INTO bmi_records
        (name,weight,height,bmi,category)

        VALUES(?,?,?,?,?)

        """,
        (
            name,
            weight,
            height,
            bmi,
            category
        ))

        conn.commit()

        return True


    except sqlite3.Error as e:

        print(e)

        return False





def get_records(name):

    try:

        cursor.execute("""
        SELECT
        id,
        date,
        weight,
        height,
        bmi,
        category

        FROM bmi_records

        WHERE name=?

        ORDER BY date DESC

        """,(name,))


        return cursor.fetchall()


    except sqlite3.Error as e:

        print(e)

        return []





def get_all_records():

    try:

        cursor.execute("""
        SELECT
        id,
        name,
        weight,
        height,
        bmi,
        category,
        date

        FROM bmi_records

        ORDER BY date DESC

        """)


        return cursor.fetchall()


    except:

        return []





# =================================
# DASHBOARD STATISTICS
# =================================


def dashboard_statistics():


    try:

        cursor.execute("""
        SELECT
        COUNT(*),
        AVG(bmi),
        MAX(bmi),
        MIN(bmi)

        FROM bmi_records

        """)


        result = cursor.fetchone()


        if result[0] == 0:

            return(
                0,
                0,
                0,
                0
            )


        return result


    except:

        return(
            0,
            0,
            0,
            0
        )





def get_statistics(name):


    try:

        cursor.execute("""
        SELECT

        COUNT(*),
        MAX(bmi),
        MIN(bmi),
        AVG(bmi)

        FROM bmi_records

        WHERE name=?

        """,(name,))


        data=cursor.fetchone()


        if data[0]==0:

            return(
                0,
                0,
                0,
                0
            )


        return data


    except:

        return(
            0,
            0,
            0,
            0
        )





# =================================
# UPDATE BMI RECORD
# =================================


def update_record(
        record_id,
        name,
        weight,
        height,
        bmi,
        category):


    try:

        cursor.execute("""
        UPDATE bmi_records

        SET
        name=?,
        weight=?,
        height=?,
        bmi=?,
        category=?

        WHERE id=?

        """,
        (
            name,
            weight,
            height,
            bmi,
            category,
            record_id
        ))


        conn.commit()

        return True


    except:

        return False





# =================================
# DELETE RECORD
# =================================


def delete_record(record_id):

    try:

        cursor.execute(
        """
        DELETE FROM bmi_records
        WHERE id=?
        """,
        (record_id,))


        conn.commit()


        if cursor.rowcount==0:

            return False


        return True


    except:

        return False





# =================================
# USER PROFILE FUNCTIONS
# =================================


def save_profile(
        name,
        age,
        gender,
        email,
        phone):


    try:

        cursor.execute("""
        INSERT INTO user_profile

        (name,age,gender,email,phone)

        VALUES(?,?,?,?,?)

        """,
        (
            name,
            age,
            gender,
            email,
            phone
        ))


        conn.commit()

        return True


    except Exception as e:

        print(e)

        return False





def get_profile(name):


    cursor.execute("""
    SELECT *

    FROM user_profile

    WHERE name=?

    """,
    (name,))


    return cursor.fetchone()





def update_profile(
        name,
        age,
        gender,
        email,
        phone):


    cursor.execute("""
    UPDATE user_profile

    SET
    age=?,
    gender=?,
    email=?,
    phone=?

    WHERE name=?

    """,
    (
        age,
        gender,
        email,
        phone,
        name
    ))


    conn.commit()





# =================================
# BMI GRAPH DATA
# =================================


def get_bmi_progress(name):


    cursor.execute("""
    SELECT
    date,
    bmi

    FROM bmi_records

    WHERE name=?

    ORDER BY date

    """,
    (name,))


    return cursor.fetchall()





# =================================
# EXPORT CSV
# =================================


def export_csv(filename="BMI_Report.csv"):


    try:

        records=get_all_records()


        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:


            writer=csv.writer(file)


            writer.writerow(
            [
            "ID",
            "Name",
            "Weight",
            "Height",
            "BMI",
            "Category",
            "Date"
            ])


            writer.writerows(records)



        return True


    except Exception as e:

        print(e)

        return False





# =================================
# Close Database
# =================================


def close_connection():

    conn.close()




# Test
if __name__=="__main__":

    print(
        "Database Connected Successfully"
    )

    print(
        dashboard_statistics()
    )