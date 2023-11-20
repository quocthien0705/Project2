import psycopg2 as ps
import pandas as pd

connectDB = ps.connect(
    host="a-3.postgres.database.azure.com",
    dbname="project",
    user="Project_Health_Care_System",
    password="@healthcare2",
    port=5432
)

cursor = connectDB.cursor()

cursor.execute(
    """
    CREATE TABLE user_account(
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(50),
        password VARCHAR(50),
        email VARCHAR(70)
    )
    """
)

cursor.execute(
    """
    INSERT INTO user_account(
        user_name,
        password,
        email
    )
    VALUES 
        ('quocthien0705', 'thien2002', 'thien.pham07052002@hcmut.edu.vn'),
        ('quochuy2510', 'quochuy2002', 'huy.doanquoc2510@hcmut.edu.vn')
    """
)

cursor.execute(
    """
    CREATE TABLE profile_of_patient(
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100),
        dob VARCHAR(10),
        sex VARCHAR(10),
        height VARCHAR(10),
        weight VARCHAR(10),
        phone VARCHAR(50),
        insur_number VARCHAR(50),
        address VARCHAR(200),
        note TEXT
    )
    """
)
cursor.execute(
    """
    INSERT INTO profile_of_patient(
        fullname,
        dob,
        sex,
        height,
        weight,
        phone,
        insur_number,
        address,
        note
    )
    VALUES 
        ('Pham Huynh Quoc Thien', '07/05/2002', 'Male', '169', '88', '0398955928', '2012100', '2/76 Thien Phuoc, Ward 9, Tan Binh District', ''),
        ('Steven Crawford', '08/01/2000', 'Female', '172', '75', '4876084561', '796977', '5972 Warren Square Apt. 400, Jacksonmouth, LA', ''),
        ('David Schneider', '04/12/1997', 'Male', '194', '90', '6966106701', '422083', '67386 Rivera Courts, New Kevin, MD', ''),
        ('Gina Dickerson', '07/03/1966', 'Female', '160', '52', '001766980171804920', '935094', '029 Gray Square Suite 269, East Dakota, MD', ''),
        ('Jennifer Taylor', '18/09/2023', 'Male', '183', '70', '5002042191', '489663', '7342 Kevin Run Apt. 597, Kyleborough, GU', ''),
        ('Kyle Harris', '27/04/1987', 'Male', '182', '70', '6568619794', '434187', '7679 Arnold Corners, East Andrewview, VI', '')
    """
)
connectDB.commit()


# connectDB.commit()

# def check_login(username, password):
#     cursor.execute(
#     """
#     SELECT * FROM users WHERE user_name = %s and password = %s
#     """,
#     (username,password)
#     )
#     user = cursor.fetchone() 
#     if user:
#         print("login success")
#         return True
        
#     else: 
#         print("login failure")
#         return False   
# username = "quocthien3240705"
# password = "thien2002"
# if check_login(username, password):
#     pass
# else:
#     print("no pass")
#     pass
    

# cursor.execute("SELECT * FROM users")

# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# df = pd.read_sql_query("SELECT * FROM users", connectDB)
# df.to_excel("employees.xlsx", index=False)

# cursor.close()
# connectDB.close()