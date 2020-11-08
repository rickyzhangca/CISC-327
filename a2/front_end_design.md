# CISC 327 A2 - Front End Design

![alt text](https://github.com/rickyzhangca/CISC-327/blob/a2-report/a2/frontend_architecture_diagram.png)

## Overall Structure 

The Frontend of the SeekTicket application contains four modules including, sessions module, helpers module, exceptions module, and main module.

The sessions module was constructed in an Object Oriented Structure. The base class sessions claimed the general structure of each sessions. Each module contains a username which will be set as None when the user have not logged in. The routing function inside each session’s class returns a new session object that the page will load to next. The operate functions interacts with user and the data storage with regarding helper functions.

Helpers including, resources helper, transactions helper, user IO helper contains static methods are to be interact by each session. Exceptions will be thrown when the unacceptable user input received.

The main function within the main module maintains the overall process of creating the next session object and load it into current_session and operate. The current_session object will be destroyed after it operates. The application ends when the user enters the ‘exits’ command and the next session is been loaded as None.

## Classes and Methods

### Register

| Classes/Methods                                                            | Description                                                                  |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `RegisterSession`                                                          | An UnloggedSession that asks for user information to register                |
| `RegisterSession.operate(self)`                                            | The main behaviors of registering, asking for email, user name, and password |
| `RegisterSession. checkExistence(self,user_name, user_email)`              | Check if the given email has been used in the user data `user.csv`           |
| `RegisterSession. addNewUser(self, user_name, user_email, user_password) ` | Add new `register` user transaction when all inputs are valid.               |
