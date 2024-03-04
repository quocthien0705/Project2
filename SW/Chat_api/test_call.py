#https://learn.microsoft.com/vi-vn/azure/communication-services/samples/chat-hero-sample
    ## Next step
# Create a chat client
# Create a thread with two users
# Send a message to the thread
# Receive messages from a thread
# Remove Users from a thread
import os
from azure.communication.chat import ChatClient, CommunicationTokenCredential
from datetime import datetime, timedelta
from azure.communication.chat import ChatMessageType
from azure.communication.identity import CommunicationIdentityClient
from azure.communication.chat import ChatParticipant

try:
	print('Azure Communication Services - Chat Quickstart')
	# Create a chat client
	endpoint = "https://healthcare.asiapacific.communication.azure.com/"
	chat_client = ChatClient(endpoint, CommunicationTokenCredential("eyJhbGciOiJSUzI1NiIsImtpZCI6IjYwNUVCMzFEMzBBMjBEQkRBNTMxODU2MkM4QTM2RDFCMzIyMkE2MTkiLCJ4NXQiOiJZRjZ6SFRDaURiMmxNWVZpeUtOdEd6SWlwaGsiLCJ0eXAiOiJKV1QifQ.eyJza3lwZWlkIjoiYWNzOjE0MmVkZjM1LTQwMDgtNGRjYi1iNWYyLWM5MWMzMzIxYjk5OV8wMDAwMDAxZS1hOGYyLWY5ZDYtODk3NS1jOTNhMGQwMGE1YWUiLCJzY3AiOjE3OTIsImNzaSI6IjE3MDk1NDkxMTQiLCJleHAiOjE3MDk2MzU1MTQsInJnbiI6ImFwYWMiLCJhY3NTY29wZSI6ImNoYXQiLCJyZXNvdXJjZUlkIjoiMTQyZWRmMzUtNDAwOC00ZGNiLWI1ZjItYzkxYzMzMjFiOTk5IiwicmVzb3VyY2VMb2NhdGlvbiI6ImFzaWFwYWNpZmljIiwiaWF0IjoxNzA5NTQ5MTE0fQ.UdJ5KZEXuAkDlOlN7ZAeepsooNwH3VXTe96FHaDYKgkzb66I939uMxnZowVi6ZdoPZ3ZnQyZpfUOzFb__QamRxkpoQci8yhqZ1u8mRObCDEdYNLtEetO5g_7TPgwTYFdra4yx-A2iHtbetSJgiBGIN3I8uTjI8ef5CFjLtoyFxh5Ltnmm2IIdedhfKQPwChLz4eR8wl8y7GVPmr3pA0M3vnYXZ8XovkgUFOphD3EHru1n-SFkA0iw786riqcqT16i8yYszdlUcwqtpIr4mpbrdOXJyLMKZ9OkyERK-C1HPx9Zxntoxfgd_-c_cBsDM7LOpw7HGSRql83Sxi1npk7Eg"))

	# Start a chat thread
	topic="test topic"

	create_chat_thread_result = chat_client.create_chat_thread(topic)
	chat_thread_client = chat_client.get_chat_thread_client(create_chat_thread_result.chat_thread.id)	
	
	# Get a chat thread client
	thread_id = create_chat_thread_result.chat_thread.id
	chat_thread_client = chat_client.get_chat_thread_client(thread_id)
		
	# List all chat threads
	start_time = datetime.utcnow() - timedelta(days=2)
	
	chat_threads = chat_client.list_chat_threads(results_per_page=5, start_time=start_time)
	for chat_thread_item_page in chat_threads.by_page():
		for chat_thread_item in chat_thread_item_page:
			print(chat_thread_item)
			print('Chat Thread Id: ', chat_thread_item.id)
		
		
	# Send a message to a chat thread			
	content='hello world'
	sender_display_name='sender name'

	# specify chat message type with pre-built enumerations
	send_message_result_w_enum = chat_thread_client.send_message(content=content, sender_display_name=sender_display_name, chat_message_type=ChatMessageType.TEXT)
	print("Message sent: id: ", send_message_result_w_enum.id)		

	# Receive chat messages from a chat thread
	start_time_receive = datetime.utcnow() - timedelta(days=1)

	chat_messages = chat_thread_client.list_messages(results_per_page=1, start_time=start_time_receive)
	for chat_message_page in chat_messages.by_page():
		for chat_message in chat_message_page:
			print("ChatMessage: Id=", chat_message.id, "; Content=", chat_message.content.message)
	
	# Send read receipt
	content='read receipt'

	send_message_result = chat_thread_client.send_message(content)
	chat_thread_client.send_read_receipt(message_id=send_message_result.id)
	
	# Add a user as a participant to the chat thread
	# create 2 users
	identity_client = CommunicationIdentityClient.from_connection_string('endpoint=https://healthcare.asiapacific.communication.azure.com/;accesskey=rShmmJTbctOu093kD0GOxqirkvhaLJMd0vHnGJw0wlgxqJZqwGzaAqWQZWJ5JBDSuqfU9hdivFkD2y+wUb539Q==')
	new_users = [identity_client.create_user() for i in range(2)]
	
	
	# # conversely, you can also add an existing user to a chat thread; provided the user_id is known
	# from azure.communication.identity import CommunicationUserIdentifier
	#
	# user_id = 'some user id'
	# user_display_name = "Wilma Flinstone"
	# new_user = CommunicationUserIdentifier(user_id)
	# participant = ChatParticipant(
	#     user=new_user,
	#     display_name=user_display_name,
	#     share_history_time=datetime.utcnow())
	
	
	participants = []
	for _user in new_users:
	  chat_thread_participant = ChatParticipant(
		identifier=_user,
		display_name='Fred Flinstone',
		share_history_time=datetime.utcnow()
	 ) 
	participants.append(chat_thread_participant) 

	response = chat_thread_client.add_participants(participants)

	def decide_to_retry(error, **kwargs):
		"""
		Insert some custom logic to decide if retry is applicable based on error
		"""
		return True

	# verify if all users has been successfully added or not
	# in case of partial failures, you can retry to add all the failed participants 
	retry = [p for p, e in response if decide_to_retry(e)]
	if retry:
		chat_thread_client.add_participants(retry)
		
	chat_thread_participants = chat_thread_client.list_participants()
	for chat_thread_participant_page in chat_thread_participants.by_page():
		for chat_thread_participant in chat_thread_participant_page:
			print("ChatParticipant: ", chat_thread_participant)	
	
except Exception as ex:
    print('Exception:')
    print(ex)