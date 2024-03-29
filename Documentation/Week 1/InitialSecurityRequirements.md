# Security Requirements
---
## Encryption (SQL Server)
To ensure communication between the executable and server is safe and confidential, we need to enable encryption for our SQL server (Always Encrypt setting).

## Credentials & Password Safety
We want to be safe with how we store passwords in the SQL database, as well as how the passwords are displayed in the login section (we want them hidden with asterisks). Encryption ties into this, as we definitely need to encrypt passwords...


## Access to the Server
We must limit access such that any given executable / user is only able to call specific stored procedures based on their access level (Coaches have more permissions than Athletes). For demo version, we might not worry about this as much, but in a real-world application, this is very important! Furthermore, for the credentials to *connect* to the server, we will have to make sure they aren't publically visible to the user (ex: my current password to connect to my local SQL server is empty, so the Python script I run on my local device can easily access it).