import psycopg2 as ps
from azure.communication.chat import  ChatClient, CommunicationTokenCredential, ChatParticipant
import os
from datetime import datetime, timedelta
from azure.communication.identity import CommunicationIdentityClient, CommunicationUserIdentifier
import json
endpoint = "https://healthmonitoring.asiapacific.communication.azure.com/"
connection_string = "endpoint=https://healthmonitoring.asiapacific.communication.azure.com/;accesskey=DqSzvfVZuJ2/z7atiNAzfm0ntwIwnLav/0AbiSp6ZGEt5erKcfTTazD8vmk9xQWGJ6DOI/SF7WvV97g5uQK4HQ=="
identity_client = CommunicationIdentityClient.from_connection_string(connection_string)

def connect_to_db():
    connectDB = ps.connect(
        host="a-3.postgres.database.azure.com",
        dbname="project",
        user="Project_Health_Care_System",
        password="@healthcare2",
        port=5432
    )
    return connectDB.cursor()
cursor = connect_to_db()
'''Initialise the database'''
# cursor = connect_to_db()
# cursor.execute(
#     """
#     CREATE TABLE account_identity(
#         ID VARCHAR,
#         Display_Name VARCHAR,
#         Thread_ID VARCHAR
#     )
#     """)
# cursor.connection.commit()

#Insert data to database
def insert_identity_into_db(cursor, id_value=None, display_name=None):
    cursor.execute(
        """
        INSERT INTO account_identity (ID, Display_Name)
        VALUES (%s, %s)
        """, 
        (id_value, display_name)
    )
    cursor.connection.commit()
def insert_identity_paitent_into_db(cursor, id_value=None):
    cursor.execute(
        """
        INSERT INTO patient_account identity
        VALUES (%s)
        """, 
        (id_value)
    )
    cursor.connection.commit()    
def get_all_display_names():
    cursor = connect_to_db()

    # Load the current display name from the JSON file
    with open('token_data.json', 'r') as f:
        data = json.load(f)
    current_display_name = data['display_name']

    # Check if the current display name is in the user_account table
    cursor.execute("SELECT user_name, identity FROM user_account WHERE user_name = %s", (current_display_name,))
    row = cursor.fetchone()
    if row is not None:
        # If the current display name is in the user_account table, get all display names from the patient_account table
        cursor.execute("SELECT user_name, identity FROM patient_account")
    else:
        # If the current display name is not in the user_account table, it must be in the patient_account table
        # So, get all display names from the user_account table
        cursor.execute("SELECT user_name, identity FROM user_account")

    rows = cursor.fetchall()
    display_names = [{"display_name": row[0], "id": row[1]} for row in rows]

    return display_names
def write_display_names_to_json():
    display_names = get_all_display_names()
    with open('display_names.json', 'w') as f:
        json.dump(display_names, f)
def get_id_by_display_name(cursor, display_name):
    # Query for user_account table
    query_user_account = "SELECT identity FROM user_account WHERE user_name = %s"
    cursor.execute(query_user_account, (display_name,))
    row = cursor.fetchone()
    if row is not None:
        return row[0]

    # Query for patient_account table
    query_patient_account = "SELECT identity FROM patient_account WHERE user_name = %s"
    cursor.execute(query_patient_account, (display_name,))
    row = cursor.fetchone()
    if row is not None:
        return row[0]

    # If no match found in both tables
    return None
def insert_threadid_name_into_db(cursor,joiner_1=None  , joiner_2=None, thread_id=None, topic=None):
    sql = f"ALTER TABLE thread_manage ADD COLUMN {joiner_1} VARCHAR(255)"
    cursor.execute(sql)
    sq = f"INSERT INTO thread_manage ({joiner_1}) VALUES (%s)"
    cursor.execute(sq, (joiner_2+"|"+thread_id+"|"+topic,))
    cursor.connection.commit()
#Get values by display_name

def get_threadId_by_name(cursor, joiner_1, joiner_2):
    value_pattern = f"{joiner_2}|%"
    query = f"SELECT {joiner_1} FROM thread_manage WHERE {joiner_1} LIKE %s"
    cursor.execute(query, (value_pattern,))
    row = cursor.fetchone()
    if row is not None:
        # Split the value by "|" and get the part after "|"
        thread_id = row[0].split("|")[1] if "|" in row[0] else row[0]
        return thread_id
    else:
        return None
def add_user_to_thread(cursor, joiner_1, joiner_2, thread_id, topic):

    insert_threadid_name_into_db(cursor, joiner_1, joiner_2, thread_id, topic)
    return thread_id
def create_token_and_write_to_json(user_name):
    identity = get_id_by_display_name(cursor,user_name)
    print(identity)
    if identity is not None:
        manager = IdentityManager(connection_string)
        token = manager.get_token(identity)
        data = {
            "display_name": user_name,
            "id": identity,
            "token": token
        }
        print(os.getcwd())
        with open('token_data.json', 'w') as f:
            json.dump(data, f)
    else:
        print(f"No user found with display name {user_name}")
class IdentityManager:
    def __init__(self, connection_string):
        self.identity_client = CommunicationIdentityClient.from_connection_string(connection_string)

    def create_and_add_user_to_db(self,cursor, display_name):
        user = self.identity_client.create_user()
        id_value = user.properties['id']        
        return id_value
    def create_and_add_paitent_to_db(self,cursor, display_name):
        user = self.identity_client.create_user()
        id_value = user.properties['id']        
        return id_value
    def get_token(self, user_id):
        user = user = CommunicationUserIdentifier(user_id)
        tokenresponse = self.identity_client.get_token(user, scopes=["voip","chat"])
        return tokenresponse.token

    def create_chat_client(self, token):
        chat_client = ChatClient(endpoint, CommunicationTokenCredential(token))
        return chat_client

    def create_chat_thread_id_to_db(self,cursor,chat_client,joiner_1, joiner_2, token,  topic):
        create_chat_thread_result = chat_client.create_chat_thread(topic)
    
        chat_thread_id = create_chat_thread_result.chat_thread.id
        joiner_id = get_id_by_display_name(cursor, joiner_1)
        print("joiner_id",joiner_id)
        joiner = CommunicationUserIdentifier(joiner_id)
        print("joiner",joiner)
        participant = ChatParticipant(
        identifier=joiner,
        display_name=joiner_2,
        share_history_time=datetime.utcnow()
    )   
        print("participant",participant)
        chat_thread_client = chat_client.get_chat_thread_client(chat_thread_id)
        print("chat_thread_id",chat_thread_id)
        
        chat_thread_client.add_participants([participant])
        insert_threadid_name_into_db(cursor,joiner_1, joiner_2,thread_id=chat_thread_id, topic=joiner_1+"-"+joiner_2)
        return chat_thread_id

# id_value, display_name_value, thread_id_value = create_and_add_user_to_db(cursor, 'Thien1', 'test topic')
# manager = IdentityManager(connection_string)
# user_name = "huy1"
# user_id = get_id_by_display_name(cursor, "huy1")
# token = manager.get_token(user_id)
# print("token",token)
# chat_client = manager.create_chat_client(token)
# thread_id = get_threadId_by_name(cursor, "huy1", "huy3")
# print("thread_id",thread_id)
print(get_threadId_by_name(cursor, "huy1", "huy3"))
