# CISC 327 A2 - Front End Design

## Overall Structure 



## Classes and Methods

### Register

| Classes/Methods                                                            | Description                                                                  |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `RegisterSession`                                                          | An UnloggedSession that asks for user information to register                |
| `RegisterSession.operate(self)`                                            | The main behaviors of registering, asking for email, user name, and password |
| `RegisterSession. checkExistence(self,user_name, user_email)`              | Check if the given email has been used in the user data `user.csv`           |
| `RegisterSession. addNewUser(self, user_name, user_email, user_password) ` | Add new `register` user transaction when all inputs are valid.               |