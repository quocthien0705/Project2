// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

import { AzureCommunicationTokenCredential } from '@azure/communication-common';
import { ChatClient, CreateChatThreadOptions, CreateChatThreadRequest } from '@azure/communication-chat';
import { getEndpoint } from '../envHelper';
import { getAdminUser, getToken } from '../identityClient';
const pgp = require("pg-promise")();

const client = pgp({
    host: 'a-3.postgres.database.azure.com',
    port: 5432,
    database: 'project',
    user: 'Project_Health_Care_System',
    password: '@healthcare2',
    ssl: {
        rejectUnauthorized: false,
    },
});
const connect_db = async () => {
    try {
        await client.connect();
        console.log("Connected to the database");
    } catch (error) {
        console.log("Error connecting to the database");
    }
};

const getDoctor_ThreadIdByName =  async (name1: string, name2: string) => {
  const valuePattern = `${name2}|%`;
  const query = `SELECT ${name1} FROM docter_threadmanage WHERE ${name1} LIKE $1`;
  const values = [valuePattern];

  connect_db();
  
  const res = await client.any(query, values);
  console.log("bug1");
  console.log(res);
  const str = res[0][name1];
  const parts = str.split('|');
  let t;
  if (parts.length > 2) {
      t = parts[1]; // Get the second part, which is the text between the '|' characters
  } else {
      t = str;
  }
  return t;
  
};
const get_PatientId_by_Name =  async (displayName:string) => {
  connect_db();
  const queryUserAccount = 'SELECT identity FROM patient_account WHERE user_name = $1';
  let res = await client.any(queryUserAccount, [displayName]);
  let user_id;
  if (res.length > 0) {
      user_id = res[0].identity;
  }    
  // Create an identity
  return user_id;
}
export const insert_Doctor_ThreadIdNameIntoDb = async (
  name1: string | null = null, 
  name2: string | null = null, 
  thread_id: string | null = null, 
  topic: string | null = null
): Promise<string | undefined> => {
  // Check if column exists
  const checkColumnExists = `SELECT column_name FROM information_schema.columns WHERE table_name='Docter_ThreadManage' AND column_name='${name1}';`;
  const columnExists = await client.any(checkColumnExists);
  // If column does not exist, add it
  // Code missing here

  // Check if name2 already exists in the column
  let checkJoiner2Exists = `SELECT * FROM Docter_ThreadManage WHERE ${name1} LIKE '%${name2}%'`;
  let joiner2Exists = await client.any(checkJoiner2Exists);

  if (joiner2Exists.length > 0) {
    console.log(`name2: ${name2} already exists in column: ${name1}`);
    // Extract the thread ID from the existing record
    let existingRecord = joiner2Exists.rows[0][name1];
    console.log(existingRecord);
    let existingThreadId = existingRecord.split("|")[1];
    return existingThreadId;
  }

  // Insert data into the column
  let sq = `INSERT INTO Docter_ThreadManage (${name1}) VALUES ($1)`;
  await client.any(sq, [name2 + "|" + thread_id + "|" + topic]);

  let sqq = `INSERT INTO patient_threadmanage (${name2}) VALUES ($1)`;
  await client.any(sqq, [name1 + "|" + thread_id + "|" + topic]);

  return thread_id;
}
export const createThread = async (name1:string, name2:string): Promise<string> =>{
    // Check if name2 already exists in the name1 column
  console.log(name1,name2);
  let checkJoinerExists = `SELECT * FROM docter_threadmanage WHERE ${name1} LIKE '%${name2}%'`;
  let joinerExists = await client.any(checkJoinerExists);

  if (joinerExists && joinerExists.length > 0) {
    console.log(`Joiner: ${name2} already exists in ${name1} column. Not creating a new chat thread.`);
    // Extract the thread ID from the existing record
    let existingRecord = joinerExists[0][name1];
    if (existingRecord) {
      console.log(existingRecord);
      let existingThreadId = existingRecord.split("|")[1];
      console.log(existingThreadId);
      return existingThreadId;
    } else {
      console.error(`Column ${name1} does not exist in the returned rows.`);
      // Handle the error appropriately here
      return;
    }
  }
  let joiner2_id = await get_PatientId_by_Name(name2);
  let topic = "Hello!";
  const user = await getAdminUser();
  const name2_id = await get_PatientId_by_Name(name2);
  const credential = new AzureCommunicationTokenCredential({
    tokenRefresher: async () => (await getToken(user, ['chat', 'voip'])).token,
    refreshProactively: true
  });
  const chatClient = new ChatClient(getEndpoint(), credential);
  
  const request: CreateChatThreadRequest = {
    topic:  topic
  };
  const options: CreateChatThreadOptions = {
    participants: [
      {
        id: { communicationUserId: name2_id },
        displayName: name2
      }
    ]
  };
  const result = await chatClient.createChatThread(request, options);

  const threadID = result.chatThread?.id;
  insert_Doctor_ThreadIdNameIntoDb( name1, name2, threadID, topic);
  return threadID;
}
// export const createThread = async (name1:string,name2:string): Promise<string> => {
//   let checkJoinerExists = `SELECT * FROM patient_threadmanage WHERE ${name1} LIKE '%${name2}%'`;
//   let joinerExists = await client.query(checkJoinerExists);
//   const user = await getAdminUser();
//   const name2_id = await get_PatientId_by_Name(name2);
//   const credential = new AzureCommunicationTokenCredential({
//     tokenRefresher: async () => (await getToken(user, ['chat', 'voip'])).token,
//     refreshProactively: true
//   });
//   const chatClient = new ChatClient(getEndpoint(), credential);

//   const request: CreateChatThreadRequest = {
//     topic:  'Your Chat sample'
//   };
//   const options: CreateChatThreadOptions = {
//     participants: [
//       {
//         id: { communicationUserId: name2_id },
//         displayName: name2
//       }
//     ]
//   };
//   const result = await chatClient.createChatThread(request, options);

//   const threadID = result.chatThread?.id;
//   const threadID = await getDoctor_ThreadIdByName(name1, name2);
//   console.log(threadID);
//   return threadID;
// };
