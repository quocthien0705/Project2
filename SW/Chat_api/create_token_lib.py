import os
from datetime import timedelta
from azure.communication.identity import CommunicationIdentityClient, CommunicationUserIdentifier

# This code demonstrates how to retrieve your connection string
# from an environment variable.
import psycopg2 as ps
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
connection_string = "endpoint=https://healthmonitoring.asiapacific.communication.azure.com/;accesskey=DqSzvfVZuJ2/z7atiNAzfm0ntwIwnLav/0AbiSp6ZGEt5erKcfTTazD8vmk9xQWGJ6DOI/SF7WvV97g5uQK4HQ=="
# Instantiate the identity client
# client = CommunicationIdentityClient.from_connection_string(connection_string)

# identity = client.create_user()
# print("\nCreated an identity with ID: " + identity.properties['id'])
# insert_new_user(identity.properties['id'])
b=get_third_row_id()
print(b)

# # Issue an access token with a validity of 24 hours and the "voip" scope for an identity
# token_result = client.get_token(identity, ["voip"])
# print("\nIssued an access token with 'voip' scope that expires at " + token_result.expires_on + ":")
# print(token_result.token)
