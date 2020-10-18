|                        Specification                         | Test ID | Purpose                                                      |                        Test Procedure                        |                        Expect Output                         |
| :----------------------------------------------------------: | :-----: | :----------------------------------------------------------- | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  User must be logged in to starts a ticket selling session   | R4.0.1  | Checki if the selling command invalid when user has not logged in |               Starts a ticket selling session                |        Invaild command, user must be logged in first         |
|                                                              | R4.0.2  | Checki if the selling session start  when user has not logged in |           Login;  Starts a ticket selling session            | Selling Session Starting...; "Please enter the ticket name:" |
| The name of the ticket has to be alphanumeric-only, space allowed only if it is not the first or the last character, and no longer than 60 characters | R4.1.1  | Check if a valid ticket name can be accepted in the selling session | Login;  Starts a ticket selling session;   Enter valid ticket name (e.g. [Hamilton]) | "Ticket Name: \Ticket name;  Please enter the ticket quantity:" |
|                                                              | R4.1.2  | Check if a not alphanumeric-only ticket name not be accepted in the selling session | Login;  Starts a ticket selling session;  Enter not alphanumeric-only ticket name (e.g. [HH**]') | "Invalid! The name format is alphanumeric-only; Please enter the ticket name:" |
|                                                              | R4.1.3  | Check if the first or the last character of name is space not be accepted in the selling session | Login;  Starts a ticket selling session;  Enter ticket name with space is the first or the last character (e.g. [ Hamilton ]) | "Invalid! First Character or Last Characte cannot be space; Please enter the ticket name:" |
|                                                              | R4.1.4  | Check if the name of the ticket is longer than 60 characters not be accepted in the selling session | Login;  Starts a ticket selling session;  Enter ticket name which is longer than 60 characters | "Invalid! Name should shorter than 60 characters; Please enter the ticket name:" |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R4.2.1  | Check if the valid quantity can be accepted in the selling session | Login; Starts a ticket selling session; Enter valid ticket name; Enter valid quantity (e.g. [2]) | "[Ticket Name: \Ticket name]; [Ticket Quantity: \Ticket quantity]; Please enter the ticket price:" |
|                                                              | R4.2.2  | Check if the quantity of the tickets is more than 100 not be accepted in the selling session | Login; Starts a ticket selling session; Enter valid ticket name; Enter quantity more than 100 (e.g. [101]) | "Invalid! The quantity of the tickets has to be less than 100; Please enter the ticket quantity:" |
|                                                              | R4.2.3  | Check if the quantity of the tickets is less than or equal to 0 not be accepted in the selling session | Login; Starts a ticket selling session; Enter valid ticket name; Enter quantity less than or equal to 0 (e.g. [0]) | "Invalid! The quantity of the tickets has to be more than 0; Please enter the ticket quantity:" |
|     The price of the ticket has to be of range [10, 100]     | R4.3.1  | Check if the valid price can be accepted in the selling session | Login;  Starts a ticket selling session;  Enter valid ticket name; Enter valid ticket quantity; Enter valid ticket price (e.g. 43) | "[Ticket Name: \Ticket name]; [Ticket Quantity: \Ticket quantity]; [Ticket Price: \Ticket price];  Please enter the ticket date:" |
|                                                              | R4.3.2  | Check if the price of the ticket is not in range [10, 100] not be accepted in the selling session | Login;  Starts a ticket selling session;  Enter valid ticket name; Enter valid ticket quantity; Enter invalid ticket price not in the range [10, 100] (e.g. 3) | "Invalid! The price of the ticket has to be of range [10, 100]; Please enter the ticket price:" |
| The date of the ticket must be given in the format YYYYMMDD (e.g. 20200901) | R4.4.1  | Check if the valid date can be accepted in the selling session | Login;  Starts a ticket selling session;  Enter valid ticket name; Enter valid ticket quantity; Enter valid ticket price; Enter valid ticket date (e.g. 20200901) |  Append a new registration transaction if successfully sold  |
|                                                              | R4.4.2  | Check if the incorrect format date not be accepted in the selling session | Login;  Starts a ticket selling session;  Enter valid ticket name; Enter valid ticket quantity; Enter valid ticket price; Enter incorrect format  ticket date (e.g. 09012020) | "Invalid! The date of the ticket must be given in the format YYYYMMDD (e.g. 20200901); Please enter the ticket date:" |


