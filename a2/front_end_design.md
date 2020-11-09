# CISC 327 A2 - Front End Design

![alt text](https://github.com/rickyzhangca/CISC-327/blob/a2-report/a2/frontend_architecture_diagram.png)

## Overall Structure 

The Frontend of the SeetGeek application contains four modules including, sessions module, helpers module, exceptions module, and main module.

The sessions module was constructed in an Object Oriented Structure. The base class sessions claimed the general structure of each sessions. Each module contains a username which will be set as None when the user have not logged in. The routing function inside each session’s class returns a new session object that the page will load to next. The operate functions interacts with user and the data storage with regarding helper functions.

Helpers including, resources helper, transactions helper, user IO helper contains static methods are to be interact by each session. Exceptions will be thrown when the unacceptable user input received.

The main function within the main module maintains the overall process of creating the next session object and load it into current_session and operate. The current_session object will be destroyed after it operates. The application ends when the user enters the ‘exits’ command and the next session is been loaded as None.

## Classes and Methods

### Resources Helper

| Classes/Methods                                    | Description                                                                                               |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `ResourcesHelper`                                  | An class with static methods that helps retrieving user and tickiet data from`user.csv` and`tickert.csv`. |
| `ResourcesHelper.loadUserInfo(user_file_path)`     | Load user data from `user.csv` given a file path and save to `helpers.user_info`                          |
| `ResourcesHelper.loadTicketInfo(ticket_file_path)` | Load ticket data from `ticket.csv` given a file path and save to `helpers.ticket_info`                    |
| `ResourcesHelper.getUserInfo()`                    | Return user data from`helpers.user_info`                                                                  |
| `ResourcesHelper.getTicketInfo()`                  | Return ticket data from`helpers.ticket_info`                                                              |

### User IO Helper

| Classes/Methods                       | Description                                                                                                         |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `UserIOHelper`                        | An class with static methods that are used to validate different type of user inputs.                               |
| `UserIOHelper.acceptEmail()`          | Ask the user to input an email address and validate according to RFC 5322 standard. Raise exceptions if failed.     |
| `UserIOHelper.acceptPassword()`       | Ask the user to input a password and validate according to the requirements. Raise exceptions if failed.            |
| `UserIOHelper.acceptPassword2()`      | Ask the user to input a string.                                                                                     |
| `UserIOHelperacceptTicketName()`      | Ask the user to input a ticket name and validate according to the requirements. Raise exceptions if failed.         |
| `UserIOHelper.acceptTicketQuantity()` | Ask the user to input a quantity of tickets and validate according to the requirements. Raise exceptions if failed. |
| `UserIOHelper.acceptTicketPrice()`    | Ask the user to input a price for tickets and validate according to the requirements. Raise exceptions if failed.   |
| `UserIOHelper.acceptDate()`           | Ask the user to input a date and validate according to the requirements. Raise exceptions if failed.                |
| `UserIOHelper.acceptUserName()`       | Ask the user to input a user name and validate according to the requirements. Raise exceptions if failed.           |

### Transactions Helper

| Classes/Methods                                                                                               | Description                                                                                                     |
| ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `TransactionsHelper`                                                                                          | An class with static methods that writes transactions.                                                          |
| `TransactionsHelper.saveTransactions(location)`                                                               | Write transactions to a given path. Append if the file already exists, otherwise create a new transaction file. |
| `TransactionsHelper.newUserTransaction(transaction_name, user_name, user_email, user_password, balance)`      | Append a new user transaction to `helpers. transactions`.                                                       |
| `TransactionsHelper. newTicketTransaction(transaction_name, user_name, ticket_name, ticket_price, quantity) ` | Append a new ticket transaction to `helpers. transactions`.                                                     |

### Register

| Classes/Methods                                                            | Description                                                                  |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `RegisterSession`                                                          | An UnloggedSession that asks for user information to register                |
| `RegisterSession.operate(self)`                                            | The main behaviors of registering, asking for email, user name, and password |
| `RegisterSession.checkExistence(self,user_name, user_email)`               | Check if the given email has been used in the user data `user.csv`           |
| `RegisterSession.addNewUser(self, user_name, user_email, user_password) `  | Add new `register` user transaction when all inputs are valid                |

### Buy

| Classes/Methods                                              | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `BuySession`                                                 | A loggedSession that asks for use input ticket information for sale |
| `BuySession.operate(self)`                                   | The main behaviors of registering, asking for ticket_name and ticket_quantity |
| `BuySession.printTicketList(self)`                           | Showing the information on available ticket sales           |
| `BuySession.checkBalance(self, ticket_price, ticket_quantity)` | Check if the balance in the user account is enough to buy tickets or not |
| `BuySession.processOrder(self, ticket_name, ticket_price, ticket_quantity)` | Append a new registration transaction if successful buying   |

### Sell

| Classes/Methods                                              | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `SellSession`                                                | A loggedSession that asks for use input ticket information for sale |
| `SellSession.operate(self)`                                  | The main behaviors of selling, asking for ticket_name, ticket_price, ticket_quantity and ticket_date |
| `SellSession.addNewTicket(self, ticket_name, ticket_price, ticket_quantity)` | Append a new registration transaction if successful selling  |

### Login

| Classes/Methods                                                            | Description                                                                  |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `LoginSession`                                                             | An UnloggedSession that asks for user information to login                   |
| `LoginSession.routing(self) `                                              | Route to a logged in landing session if the login was successful             |
| `LoginSession.operate(self)`                                               | The main behaviors of login, asking for email and password then authorize    |
| `LoginSession.authorize(self,email, password)`                             | Authorize email and password the user inputed. Setup username                |

### Logout

| Classes/Methods                                                            | Description                                                                  |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `LogoutSession`                                                            | An loggedSession that loggout the current user                               |
| `LogoutSession.routing(self) `                                             | Route to a unlogged in landing session                                       |
| `LogoutSession.operate(self)`                                              | Notice the user that the logout was successfuly                              |
