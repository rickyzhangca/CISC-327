# CISC 327 A2 - Front End Design



## Overall Structure 

The Backend of the SeetGeek application contains six modules including, config module, controller module, entities module, repositories module, service module and main module.

---------continue to update----------------

The main function within the main module maintains the overall process of retrieving user and ticket information from each transaction and update into `user.csv` and `ticket.csv`.

## Classes and Methods

### UserResourcesEntity

| Classes/Methods                                    | Description                                           |
| -------------------------------------------------- | ----------------------------------------------------- |
| `UserResourcesEntity`                              | A class load user information and update the balance. |
| `UserResourcesEntity.updatebalance(self, balance)` | Update the new balance of user information.           |

### User IO Helper

| Classes/Methods                                        | Description                                              |
| ------------------------------------------------------ | -------------------------------------------------------- |
| `TicketResourcesEntity`                                | A class load ticket information and update the quantity. |
| `TicketResourcesEntity.updateQuantity(self, quantity)` | Update the new quantity of ticket information.           |

### UserTransactionsEntity

| Classes/Methods          | Description                                           |
| ------------------------ | ----------------------------------------------------- |
| `UserTransactionsEntity` | A class load user information from transaction files. |

### TicketTransactionsEntity

| Classes/Methods            | Description                                             |
| -------------------------- | ------------------------------------------------------- |
| `TicketTransactionsEntity` | A class load ticket information from transaction files. |

### Repository

| Classes/Methods                        | Description                                         |
| -------------------------------------- | --------------------------------------------------- |
| `Repository`                           | A class load the information and update any change. |
| `Repository.save(self, new_entity) `   | Append the new infromation find by `findBy`.        |
| `Repository.findBy(self, entity_id)`   | Determine if the `entity_id` is a new information.  |
| `Repository.deleteBy(self, entity_id)` | Delete the `entity_id `.                            |
| `Repository.readFile(self)`            | Read the file.                                      |
| `Repository.storeFile(self)`           | Write the information into a file.                  |

### UserResourcesRepository

| Classes/Methods            | Description                   |
| -------------------------- | ----------------------------- |
| `TicketTransactionsEntity` | A class load user informatio. |

### TicketResourcesRepository

| Classes/Methods            | Description                      |
| -------------------------- | -------------------------------- |
| `TicketTransactionsEntity` | A class load ticket information. |

### TransactionsRepository

| Classes/Methods            | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| `TicketTransactionsEntity` | A class load new ticket information and new user information from transaction files. |

### Service

| Classes/Methods                               | Description                                                  |
| --------------------------------------------- | ------------------------------------------------------------ |
| `Service`                                     | A class determine the kind of information and update into `user.csv`  or `ticket.csv`. |
| `Service.processTransactions(self) `          | Determine the kind of information, register, sell or buy, and executing the corresponding function. |
| `Service.updateDatabase(self)`                | Update information into `ticket.csv`, `user.csv` and each transaction files. |
| `Service.addUser(self, transaction)`          | Add new register's information.                              |
| `Service.buyTicket(self, transaction)`        | Update the corresponding user's balance and ticket's quantity. |
| `Service.sellUpdateTicket(self, transaction)` | Add new ticket information.                                  |
| `Service.getUserEmail(self, user_name)`       | Return the `user_email` which corresponds ot `user_name`     |

### 