from azure.communication.identity import CommunicationIdentityClient
from azure.communication.chat import  ChatClient, CommunicationTokenCredential
import os
from datetime import timedelta
from azure.communication.identity import CommunicationIdentityClient, CommunicationUserIdentifier
import json
# This code demonstrates how to retrieve your connection string
# from an environment variable.
import psycopg2 as ps
from datetime import datetime, timedelta
from azure.communication.chat import ChatParticipant
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
def insert_new_user(identity):
    cursor = connect_to_db()
    cursor.execute(
        """
        INSERT INTO identity(
            ID
        )
        VALUES (%s)
        """, 
        (identity,)
    )
    cursor.connection.commit()
def get_data_from_table(table_name):
    cursor = connect_to_db()
    cursor.execute(f"SELECT ID FROM {table_name}")
    data = cursor.fetchall()
def get_third_row_id():
    cursor = connect_to_db()
    cursor.execute("SELECT ID FROM identity")
    rows = cursor.fetchall()
    if len(rows) >= 3:
        return rows[2][0]  # Rows are 0-indexed, so the third row is at index 2
    else:
        return None  # Return None if there are less than 3 rows
    return data
def create_chat_client(token):
    chat_client = ChatClient(endpoint, CommunicationTokenCredential(token))
    # [END create_chat_client]
    return chat_client
def create_chat_thread_id(chat_client,topic):
    create_chat_thread_result = chat_client.create_chat_thread(topic)
   
    return create_chat_thread_result.chat_thread.id
def get_identity_by_display_name(display_name):
    cursor = connect_to_db()
    cursor.execute("SELECT ID FROM account_identity WHERE display_name = %s", (display_name,))
    row = cursor.fetchone()
    if row is not None:
        return row[0]
    else:
        return None

def create_token_and_write_to_json(display_name):
    identity = get_identity_by_display_name(display_name)
    print(identity)
    if identity is not None:
        manager = IdentityManager(connection_string)
        user = CommunicationUserIdentifier(identity)
        token = manager.get_token(user)
        data = {
            "display_name": display_name,
            "id": identity,
            "token": token
        }
        with open('token_data.json', 'w') as f:
            json.dump(data, f)
    else:
        print(f"No user found with display name {display_name}")
        
def get_all_display_names():
    cursor = connect_to_db()
    cursor.execute("SELECT display_name, ID FROM account_identity")
    rows = cursor.fetchall()
    display_names = [{"display_name": row[0], "id": row[1]} for row in rows]

    # Load the current display name from the JSON file
    with open('token_data.json', 'r') as f:
        data = json.load(f)
    current_display_name = data['display_name']

    # Remove the current display name from the list
    display_names = [d for d in display_names if d["display_name"] != current_display_name]

    return display_names
def write_display_names_to_json():
    display_names = get_all_display_names()
    with open('display_names.json', 'w') as f:
        json.dump(display_names, f)
        
class IdentityManager:
    def __init__(self, connection_string):
        self.identity_client = CommunicationIdentityClient.from_connection_string(connection_string)

    def create_user(self):
        user = self.identity_client.create_user()
        insert_new_user(user.properties['id'])
        return user  # return the CommunicationUserIdentifier object

    def get_token(self, user):
        tokenresponse = self.identity_client.get_token(user, scopes=["voip"])
        return tokenresponse.token

create_token_and_write_to_json('Thien1')
write_display_names_to_json()
# user = manager.create_user()
# identity1 = CommunicationUserIdentifier('8:acs:9efc7d1f-f4cf-4127-a2ca-1a57bccbe501_0000001e-f275-9583-b169-62bd4560c9fc')
# identity = CommunicationUserIdentifier('8:acs:9efc7d1f-f4cf-4127-a2ca-1a57bccbe501_0000001e-f27a-42d5-b661-62bd4560ceed')
# token = manager.get_token(identity)
# print("token",token,"\n")
# new_users = [identity_client.create_user() for i in range(2)]
# print("new_users",new_users,"\n")
# client1 = create_chat_client("eyJhbGciOiJSUzI1NiIsImtpZCI6IjYwNUVCMzFEMzBBMjBEQkRBNTMxODU2MkM4QTM2RDFCMzIyMkE2MTkiLCJ4NXQiOiJZRjZ6SFRDaURiMmxNWVZpeUtOdEd6SWlwaGsiLCJ0eXAiOiJKV1QifQ.eyJza3lwZWlkIjoiYWNzOjllZmM3ZDFmLWY0Y2YtNDEyNy1hMmNhLTFhNTdiY2NiZTUwMV8wMDAwMDAxZS1lNWY5LWM3MDEtYjY2MS02MmJkNDU2MDAxOWIiLCJzY3AiOjE3OTIsImNzaSI6IjE3MTA1NzI5NzEiLCJleHAiOjE3MTA2NTkzNzEsInJnbiI6ImFwYWMiLCJhY3NTY29wZSI6ImNoYXQiLCJyZXNvdXJjZUlkIjoiOWVmYzdkMWYtZjRjZi00MTI3LWEyY2EtMWE1N2JjY2JlNTAxIiwicmVzb3VyY2VMb2NhdGlvbiI6ImFzaWFwYWNpZmljIiwiaWF0IjoxNzEwNTcyOTcxfQ.pILWagZvaKpkT8eHcvHZ15DNQCRYpAnvqyzpsEmN-lcrWODyzdmYlsTvzRPOKcEowUgsDSYQaHuyMUqJcFWYXbbL_a_G2QuAZr-QQaVL81zVJKrvhUayaMKQGpQceeBAjOGHnWc58ZYUbNmEFzqUnlSxwS-m4QYWyBjrz64p9s294eXBJdsXbp3XE0Z7_HJk2hJZB1VRNkgMFG9THCsj2upvmAxXOft_0PDE_ooQ_SxDn4VqSOmzaWuD76Dv0VChkFkP1X_-gbFA1JNp6G-WcnovfmXBY9-6iBJjlBkGOE0vI7sJ3kpJyuwFYqOaKVq2rR3d54JV4l4Lk6OfiZgT4Q")
# print("client1",client1,"\n")
# test_topic= "test topic"
# chat_thread_client = client1.get_chat_thread_client("19:ijxGzQsyT8APoA_TDODLUIGmgXp_wi4sZpTMqfahjr01@thread.v2")
# participants = []
# for _user in new_users:
#   chat_thread_participant = ChatParticipant(
#     identifier=_user,
#     display_name='Fred Flinstone',
#     share_history_time=datetime.utcnow()
#   ) 
#   participants.append(chat_thread_participant) 

# response = chat_thread_client.add_participants(participants)
# b=chat_thread_client.send_message(content="message",sender_display_name="huy")
# chat_thread_client.send_message(content="message2",sender_display_name="huy2")
# chat_thread_client.send_message(content="message3",sender_display_name="huy3")
# update_chat_thread = chat_thread_client.update_topic("test topic")
# start_time = datetime.utcnow() - timedelta(days=2)

# chat_messages = chat_thread_client.list_messages(results_per_page=1, start_time=start_time)
# for chat_message_page in chat_messages.by_page():
#     for chat_message in chat_message_page:
#         print("ChatMessage: Id=", chat_message.id, "; Content=", chat_message.content.message, "sender" ,chat_message.sender_display_name)
# chat_thread_participants = chat_thread_client.list_participants()
# for chat_thread_participant_page in chat_thread_participants.by_page():
#     for chat_thread_participant in chat_thread_participant_page:
#         print("ChatParticipant: ", chat_thread_participant.display_name)