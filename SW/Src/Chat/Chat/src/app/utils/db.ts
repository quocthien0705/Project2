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

const getDoctor_ThreadIdByName =  async (joiner_1: string, joiner_2: string) => {
  const valuePattern = `${joiner_2}|%`;
  const query = `SELECT ${joiner_1} FROM docter_threadmanage WHERE ${joiner_1} LIKE $1`;
  const values = [valuePattern];

  connect_db();
  
  const res = await client.any(query, values);
  console.log("bug1");
  console.log(res);
  const str = res[0][joiner_1];
  const parts = str.split('|');
  let t;
  if (parts.length > 2) {
      t = parts[1]; // Get the second part, which is the text between the '|' characters
  } else {
      t = str;
  }
  return t;
  
};

// async function create_chatThread_WithDocter(joiner_1: string, joiner_2: string): Promise<string> {
//     let checkJoinerExists = `SELECT * FROM Docter_ThreadManage WHERE ${joiner_1} LIKE '%${joiner_2}%'`;
//     let joinerExists = await client.query(checkJoinerExists);
  
//     if (joinerExists.rows.length > 0) {
//       console.log(`Joiner: ${joiner_2} already exists in ${joiner_1} column. Not creating a new chat thread.`);
//       let existingRecord = joinerExists.rows[0][joiner_1];
//       let existingThreadId = existingRecord.split("|")[1];
//       return existingThreadId;
//     }
  
//     let joiner2_id = await get_PatientId_by_Name(joiner_2);
//     let topic = "Hello!";
//     const createChatThreadRequest: ChatThreadRequest = {
//       topic: topic
//     };
//     const createChatThreadOptions: ChatThreadOptions = {
//       participants: [
//         {
//           id: { communicationUserId: joiner2_id },
//           displayName: joiner_2
//         }
//       ]
//     };
//     const chatClient: ChatClient = new ChatClient(/* parameters to initialize ChatClient */);
//     const createChatThreadResult: ChatThreadResult = await chatClient.createChatThread(
//       createChatThreadRequest,
//       createChatThreadOptions
//     );
//     const threadId = createChatThreadResult.chatThread.id;
//     insert_Doctor_ThreadIdNameIntoDb(client, joiner_1, joiner_2, threadId, topic);
//     return threadId;
//   }
export const get_PatientId_by_Name =  async (displayName:string) : Promise<string> => {
    connect_db();
    const queryUserAccount = "SELECT identity FROM patient_account WHERE user_name = $1";
    let res = await client.any(queryUserAccount, [displayName]);
    let user_id;
    if (res.length > 0) {
        user_id = res[0].identity;
    }    
    // Create an identity
    return user_id;
}

async function main() {
  const a = await get_PatientId_by_Name("tess");
  console.log(a);
}

main();