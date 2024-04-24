"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.get_PatientId_by_Name = void 0;
var pgp = require("pg-promise")();
var client = pgp({
    host: 'a-3.postgres.database.azure.com',
    port: 5432,
    database: 'project',
    user: 'Project_Health_Care_System',
    password: '@healthcare2',
    ssl: {
        rejectUnauthorized: false,
    },
});
var connect_db = function () { return __awaiter(void 0, void 0, void 0, function () {
    var error_1;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                _a.trys.push([0, 2, , 3]);
                return [4 /*yield*/, client.connect()];
            case 1:
                _a.sent();
                console.log("Connected to the database");
                return [3 /*break*/, 3];
            case 2:
                error_1 = _a.sent();
                console.log("Error connecting to the database");
                return [3 /*break*/, 3];
            case 3: return [2 /*return*/];
        }
    });
}); };
var getDoctor_ThreadIdByName = function (joiner_1, joiner_2) { return __awaiter(void 0, void 0, void 0, function () {
    var valuePattern, query, values, res, str, parts, t;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                valuePattern = "".concat(joiner_2, "|%");
                query = "SELECT ".concat(joiner_1, " FROM docter_threadmanage WHERE ").concat(joiner_1, " LIKE $1");
                values = [valuePattern];
                connect_db();
                return [4 /*yield*/, client.any(query, values)];
            case 1:
                res = _a.sent();
                console.log("bug1");
                console.log(res);
                str = res[0][joiner_1];
                parts = str.split('|');
                if (parts.length > 2) {
                    t = parts[1]; // Get the second part, which is the text between the '|' characters
                }
                else {
                    t = str;
                }
                return [2 /*return*/, t];
        }
    });
}); };
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
var get_PatientId_by_Name = function (displayName) { return __awaiter(void 0, void 0, void 0, function () {
    var queryUserAccount, res, user_id;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                connect_db();
                queryUserAccount = "SELECT identity FROM patient_account WHERE user_name = $1";
                return [4 /*yield*/, client.any(queryUserAccount, [displayName])];
            case 1:
                res = _a.sent();
                if (res.length > 0) {
                    user_id = res[0].identity;
                }
                // Create an identity
                return [2 /*return*/, user_id];
        }
    });
}); };
exports.get_PatientId_by_Name = get_PatientId_by_Name;
function main() {
    return __awaiter(this, void 0, void 0, function () {
        var a;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0: return [4 /*yield*/, (0, exports.get_PatientId_by_Name)("tess")];
                case 1:
                    a = _a.sent();
                    console.log(a);
                    return [2 /*return*/];
            }
        });
    });
}
main();
