// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

import { ChatClient } from '@azure/communication-chat';
import { AzureCommunicationTokenCredential } from '@azure/communication-common';
import * as express from 'express';
import { getEndpoint } from '../lib/envHelper';
import { getAdminUser, getToken } from '../lib/identityClient';
import { get } from 'http';
import { threadId } from 'worker_threads';
// const pgp = require("pg-promise")();

// const client = pgp({
//     host: 'a-3.postgres.database.azure.com',
//     port: 5432,
//     database: 'project',
//     user: 'Project_Health_Care_System',
//     password: '@healthcare2',
//     ssl: {
//         rejectUnauthorized: false,
//     },
// });
// const connect_db = async () => {
//     try {
//         await client.connect();
//         console.log("Connected to the database");
//     } catch (error) {
//         console.log("Error connecting to the database");
//     }
// };

// const getDoctor_ThreadIdByName =  async (joiner_1: string, joiner_2: string) => {
//   const valuePattern = `${joiner_2}|%`;
//   const query = `SELECT ${joiner_1} FROM docter_threadmanage WHERE ${joiner_1} LIKE $1`;
//   const values = [valuePattern];

//   connect_db();
  
//   const res = await client.any(query, values);
//   console.log("bug1");
//   console.log(res);
//   const str = res[0][joiner_1];
//   const parts = str.split('|');
//   let t;
//   if (parts.length > 2) {
//       t = parts[1]; // Get the second part, which is the text between the '|' characters
//   } else {
//       t = str;
//   }
//   return t;
  
// };

// console.log("addUser.ts");

const router = express.Router();
interface AddUserParam {
  Id: string;
  DisplayName: string;
}

/**
 * route: /addUser/[threadId]
 *
 * purpose: Add the user to the chat thread with given threadId.
 *
 * @param threadId: id of the thread to which user needs to be added
 * @param id: id of the user as string
 * @param displayName: display name of the user as string
 *
 */

router.post('/:threadId', async function (req, res, next) {
  const addUserParam: AddUserParam = req.body;
  const threadId = req.params['threadId'];

  // create a user from the adminUserId and create a credential around that
  const credential = new AzureCommunicationTokenCredential({
    tokenRefresher: async () => (await getToken(getAdminUser(), ['chat', 'voip'])).token,
    refreshProactively: true
  });

  const chatClient = new ChatClient(getEndpoint(), credential);
  const chatThreadClient = await chatClient.getChatThreadClient(threadId);

  try {
    await chatThreadClient.addParticipants({
      participants: [
        {
          id: { communicationUserId: addUserParam.Id },
          displayName: addUserParam.DisplayName
        }
      ]
    });
    res.sendStatus(201);
  } catch (err) {
    // we will return a 404 if the thread to join is not accessible by the server user.
    // The server user needs to be in the thread in order to add someone.
    // So we are returning back that we can't find the thread to add the client user to.
    res.sendStatus(404);
  }
});

export default router;
