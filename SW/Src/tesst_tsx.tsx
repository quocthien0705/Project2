const pgp = require('pg').pgp;
const db = pgp({
    host: 'a-3.postgres.database.azure.com',
    port: 5432,
    database: 'project',
    user: 'Project_Health_Care_System',
    password: '@healthcare2',
    ssl: {
        rejectUnauthorized: false,
    },
});