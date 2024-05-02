// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

import { AzureCommunicationTokenCredential } from '@azure/communication-common';
import { ChatClient, CreateChatThreadOptions, CreateChatThreadRequest } from '@azure/communication-chat';
import { getEndpoint } from '../envHelper';
import { getAdminUser, getToken } from '../identityClient';
import tokenData from '../../../../../../Src/Video Call/token_data.json';
import { token } from 'morgan';
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
  const query = `SELECT ${name1} FROM doctor_threadmanage WHERE ${name1} LIKE $1`;
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
const get_DoctorID_by_Name =  async (displayName:string) => {
  connect_db();
  const queryUserAccount = 'SELECT identity FROM user_account WHERE user_name = $1';
  let res = await client.any(queryUserAccount, [displayName]);
  let user_id;
  if (res.length > 0) {
      user_id = res[0].identity;
  }    
  // Create an identity
  return user_id;
}

export const createThread = async (name1:string, name2:string): Promise<string> =>{
    // Check if name2 already exists in the name1 column
  let Check = null;
  let name2_id = '';
  if(tokenData.table_name == "patient_account"){
    Check = 'patient_threadmanage';
    name2_id = await get_DoctorID_by_Name(name2);
  }
  else{
    Check = 'doctor_threadmanage';
    name2_id = await get_PatientId_by_Name(name2);
  } 
  
  let checkJoinerExists = `SELECT * FROM ${Check} WHERE ${name1} LIKE '%${name2}%'`;
  let joinerExists = await client.any(checkJoinerExists);

  if (joinerExists && joinerExists.length > 0) {
    console.log(`Joiner: ${name2} already exists in ${name1} column. Not creating a new chat thread.`);  // Extract the thread ID from the existing record
    let existingRecord = joinerExists[0][name1];
    if (existingRecord) {
      console.log(existingRecord);
      let existingThreadId = existingRecord.split("|")[1];
      return existingThreadId;
    } else {
      console.error(`Column ${name1} does not exist in the returned rows.`);
      // Handle the error appropriately here
      return;
    }
  }
  let topic = "Hello!";
  const user = await getAdminUser();

  //////////////////////////
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
  if(Check == 'patient_threadmanage'){
  let sq = `INSERT INTO doctor_threadmanage (${name2}) VALUES ($1)`;
  await client.any(sq, [name1 + "|" + threadID + "|" + topic]);

  let sqq = `INSERT INTO patient_threadmanage (${name1}) VALUES ($1)`;
  await client.any(sqq, [name2 + "|" + threadID + "|" + topic]);
  }
  else{
  let sq = `INSERT INTO doctor_threadmanage (${name1}) VALUES ($1)`;
  await client.any(sq, [name2 + "|" + threadID + "|" + topic]);

  let sqq = `INSERT INTO patient_threadmanage (${name2}) VALUES ($1)`;
  await client.any(sqq, [name1 + "|" + threadID + "|" + topic]);
  }
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
