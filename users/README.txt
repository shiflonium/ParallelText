users

Registration
============
Provides functionalities for user account creation.
Extends Django's existing user creation form.
Outputs feedback to user if provided information are invalid.

Required: Username, Password, Password Confirmation, Natural Language.
Optional: Email Address, First Name, Last Name.



Login
=====
Provides functionalities for user authentication.
Outputs feedback to user if credentials are invalid.

Required: Username, Password.



Logout
======
Provides functionalities for user deauthentication.
Deauthenticates user from server.
Deletes user's session cookies for the site.



Account Management
==================
Provides functionalities for user account management.
[TODO] Displays user's information stored in the database.
[TODO] Provides functionalities for user to change their password.

