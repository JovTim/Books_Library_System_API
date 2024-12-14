\# Books and Libraries API System

\## Description A simple Books and Libraries API system, where users can
request books, manage books, and handle library information.

\## Installation \`\`\`cmd pip install -r requirements.txt \`\`\`

\## Configuration Environment variables needed:

\- \`DATABASE_URL\`: The connection string for your database (e.g.,
\`jovtim11.mysql.pythonanywhere-services.com\`). -
\`SECRET_KEY\`: A secret key used for security purposes (default:
\`apple123\`).

\## API Endpoints \| Endpoint \| Method \| Description \|
\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|
\| \`/member_requests\` \| GET \| See a list of all book requests. \| \|
\`/member_request\` \| POST \| Make a book request. \| \| \`/books\` \|
GET \| See a list of books. \| \| \`/books/\<int:id\>\` \| GET \| Check
specific book information. \| \|
\`/books?email=johnhelldiver@gmail.com&password=1234\`\| POST \| Add a
new book. Requires employee credentials (email and password). \| \|
\`/books/\<int:id\>?email=johnhelldiver@gmail.com&password=1234\` \| PUT
\| Update a book. Requires employee credentials (email and password). \|
\| \`/books/\<int:id\>?email=johnhelldiver@gmail.com&password=1234\` \|
DELETE \| Delete a book. Requires employee credentials (email and
password). \| \| \`/library\` \| GET \| See a list of all libraries and
their available books and stocks. \| \| \`/library/\<int:id\>/details\`
\| GET \| Check specific library details and their available books and
stocks. \| \| \`/library?email=johnhelldiver@gmail.com&password=1234\`
\| POST \| Add a new library. Requires employee credentials (email and
password). \| \|
\`/library/\<int:id\>?email=johnhelldiver@gmail.com&password=1234\` \|
PUT \| Update library information. Requires employee credentials (email
and password). \| \|
\`/library/\<int:id\>?email=johnhelldiver@gmail.com&password=1234\` \|
DELETE \| Delete a library. Requires employee credentials (email and
password). \|

\## Testing Instructions for running tests:

1\. \*\*Database Connection Tests\*\*:  - Ensure the database connection
is established correctly.  - Verify the integrity and validity of
database queries.

2\. \*\*API Endpoint Tests\*\*:  - Use a mock database to simulate data
and test each endpoint.  - Validate response status codes, returned
data, and edge cases.

\## Git Commit Guidelines Use conventional commits: \`\`\`bash feat: add
endpoint for book requests fix: resolve book deletion issue docs: update
configuration section test: add library details endpoint tests \`\`\`
