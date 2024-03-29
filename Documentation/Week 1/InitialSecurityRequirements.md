# Security Requirements
---
## Encryption (SQL Server)
To ensure communication between the executable and server is safe and confidential, we need to enable encryption for our SQL server (Always Encrypt setting).

## Credentials & Password Safety
We want to be safe with how we store passwords in the SQL database, as well as how the passwords are displayed in the login section (we want them hidden with asterisks). Encryption ties into this, as we definitely need to encrypt passwords...


## Access to the Server
We must limit access such that any given executable / user is only able to call specific stored procedures based on their access level (Coaches have more permissions than Athletes). For demo version, we might not worry about this as much, but in a real-world application, this is very important! Furthermore, for the credentials to *connect* to the server, we will have to make sure they aren't publically visible to the user (ex: my current password to connect to my local SQL server is empty, so the Python script I run on my local device can easily access it).

## Access to the Server (2)
Since it is legitimately impossible to fully secure a password stored on an end-user's device, end-users will have to make all communication through the medium of an HTTP server. I have copied a template of a web server for this very purpose (it is in PHP). The web server will have access to the SQL server, but nobody else will. It will query the server according to the HTTP requests from the users, which will be limited in scope based on their role as either a Coach or an Athlete. For testing purposes, we can make the code run queries on the server directly, but we will probably have to write most of our backend in PHP instead of Python unfortunately. If PHP proves to be too challenging, we might set things up in Node.JS, as it's far more simple (at least in my opinion) to create end points and there's less to worry about overall. I'd just have to find another template and figure out how to interface with the SQL server with Node.JS instead.