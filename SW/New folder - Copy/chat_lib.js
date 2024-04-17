const { AzureCommunicationTokenCredential } = require('@azure/communication-common');
const { ChatClient } = require('@azure/communication-chat');
const { CommunicationIdentityClient } = require('@azure/communication-identity');

const { Client } = require('pg');
// Your unique Azure Communication service endpoint
let endpointUrl = "https://healthmonitoring.asiapacific.communication.azure.com/";
// The user access token generated as part of the pre-requisites



const connectionString = "endpoint=https://healthmonitoring.asiapacific.communication.azure.com/;accesskey=DqSzvfVZuJ2/z7atiNAzfm0ntwIwnLav/0AbiSp6ZGEt5erKcfTTazD8vmk9xQWGJ6DOI/SF7WvV97g5uQK4HQ==";
const identityClient = new CommunicationIdentityClient(connectionString);

async function getToken(displayName)//pass the user name to get the token, return user id and token
 {
    const queryUserAccount = "SELECT identity FROM user_account WHERE user_name = $1";
    let res = await client.query(queryUserAccount, [displayName]);
    let user_id;
    if (res.rows.length > 0) {
        user_id = res.rows[0].identity;
    }
    
    // Create an identity
    const communicationUserId = user_id;
    let tokenResponse = await identityClient.getToken({ communicationUserId }, ["chat","voip"]);
    let { token, expiresOn } = tokenResponse;
    return { user_id, token };
}
async function create_chatThread(joiner1/*current log in user_id  */, joiner_1/*name of current log in user  */, joiner_2/*name of user want to chat */) // add this to create chat thread, it have check the exitsting thread by name, jo
{
    // Check if joiner_2 already exists in the joiner_1 column
    let checkJoinerExists = `SELECT * FROM thread_manage WHERE ${joiner_1} LIKE '%${joiner_2}%'`;
    let joinerExists = await client.query(checkJoinerExists);

    if (joinerExists.rows.length > 0) {
        console.log(`Joiner: ${joiner_2} already exists in ${joiner_1} column. Not creating a new chat thread.`);
        // Extract the thread ID from the existing record
        let existingRecord = joinerExists.rows[0][joiner_1];
        let existingThreadId = existingRecord.split("|")[1];
        return existingThreadId;
    }

    let topic = "Hello!";
    const createChatThreadRequest = {
        topic: topic
    };
    const createChatThreadOptions = {
        participants: [
            {
                id: { communicationUserId: joiner1 },
                displayName: 'huyy'
            }
        ]
    };
    const createChatThreadResult = await chatClient.createChatThread(
        createChatThreadRequest,
        createChatThreadOptions
    );
    const threadId = createChatThreadResult.chatThread.id;
    insertThreadIdNameIntoDb(client, joiner_1, joiner_2, threadId, topic);
    return threadId;
}
const client = new Client({
    host: 'a-3.postgres.database.azure.com',
    user: 'Project_Health_Care_System',
    password: '@healthcare2',
    database: 'project',
    port: 5432,
    ssl: {
        rejectUnauthorized: false,
    },
});
async function getThreadIdByName(client, joiner1, joiner_2) {
    const valuePattern = `${joiner_2}|%`;
    const query = `SELECT ${joiner1} FROM thread_manage WHERE ${joiner1} LIKE $1`;
    const values = [valuePattern];

    try {
        const res = await client.query(query, values);
        if (res.rows.length > 0) {
            const threadId = res.rows[0][joiner1].includes('|') ? res.rows[0][joiner1].split('|')[1] : res.rows[0][joiner1];
            return threadId;
        } else {
            return null;
        }
    } catch (err) {
        console.error(err.stack);
    }
}
async function insertThreadIdNameIntoDb(client, joiner_1 = null, joiner_2 = null, thread_id = null, topic = null) {
    // Check if column exists
    const checkColumnExists = `SELECT column_name FROM information_schema.columns WHERE table_name='thread_manage' AND column_name='${joiner_1}';`;
    const columnExists = await client.query(checkColumnExists);

    // If column does not exist, add it
    if (columnExists.rows.length === 0) {
        let sql = `ALTER TABLE thread_manage ADD COLUMN ${joiner_1} text`;
        await client.query(sql);
    }

    // Check if joiner_2 already exists in the column
    let checkJoiner2Exists = `SELECT * FROM thread_manage WHERE ${joiner_1} LIKE '%${joiner_2}%'`;
    let joiner2Exists = await client.query(checkJoiner2Exists);

    if (joiner2Exists.rows.length > 0) {
        console.log(`Joiner_2: ${joiner_2} already exists in column: ${joiner_1}`);
        // Extract the thread ID from the existing record
        let existingRecord = joiner2Exists.rows[0][joiner_1];
        let existingThreadId = existingRecord.split("|")[1];
        return existingThreadId;
    }

    // Insert data into the column
    let sq = `INSERT INTO thread_manage (${joiner_1}) VALUES ($1)`;
    await client.query(sq, [joiner_2 + "|" + thread_id + "|" + topic]);

    return thread_id;
}
client.connect(err => {
    if (err) {
        console.error('connection error', err.stack);
    } 
});
let displayName = "7";
let id, tokencreated;
let chatClient; // Declare chatClient in the outer scope

getToken(displayName).then(({ user_id, token }) => {
    id = user_id;
    tokencreated = token;
    console.log('User ID:', id);
    console.log('Token:', tokencreated);

    chatClient = new ChatClient(endpointUrl, new AzureCommunicationTokenCredential(tokencreated)); // Use chatClient instead of chatClientt
}).then(() => {
    // Call create_chatThread inside a .then to ensure it runs after getToken has finished
    create_chatThread( id,"huy190","huy121").then((threadId) => {
        console.log('Thread ID:', threadId);
    }).catch(console.error);
}).catch(console.error);

