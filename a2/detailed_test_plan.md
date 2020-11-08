# CISC 327 A2 - Detailed Test Plan

## Organization 

The current program is the SeetGeek online Customer-to-Customer ticket selling system, that Group 66 should make a test case structure for it. The main idea of SeetGeek is supporting to a registered user who can buy and sell tickets through this online application. 

Two components make the user interacts with the system through the terminal, a front-end component, and a backend component. Each component will be put to different new classifiers, '`frontend`' and ‘`backend`' because each of them is a standalone program. 

Each classifier is a category include a whole range of feature fits in. Take the '`frontend`' for example, `landing`, `login`, `register`, `buy`, `sell`, and the `update` should be put under frontend because all of them refer to the same purpose-supporting program interact with the user. So does the backend component. Then, various functions made up a feature, so this invites a new degree of separation. 

Finally, create sufficient unit test cases (legal and illegal) for each function; secondly, create sufficient integration test cases for each feature; thirdly create integration test cases  for both two components;  at the end, create a test case for the program at a whole (go through both frontend and backend)

Therefore, the deepest level of test case structure is unit test cases, corresponding to various functions that are components of classes feature no matter for backend or frontend, to verify if the individual function meets their detailed design specification.

The upper level than this is the integration test cases,  which correspond to various feature classes that go through the `frontend` or `backend`, such as `login`, `logout`, `sell`, etc,... in this program. If those feature classes can be integrated to work as a whole.

The upper level than this is the integration test case for the frontend and backend, verify if the group of feature class can be integrated to work at whole. Test if the frontend workflow meets the function specification is one of the examples for it. 

The upper level is the system test case to verify that the complete program meets the functional specification.

## Order

Approximately, the order of the test cases will follow the test case structure, which shows in question one, start at the deepest level in the structure, end at the upper level.

Start first at unit testing to verifies every single function meet the detailed design specification; secondly, integration testing verifies that the group of units, which mean feature classes, can be integrated and work, also need to meet the design specification; thirdly, complete program be verifies that meet the functional specification by system testing; finally, acceptance testing validates program that accepts by customer.

In more detail, the order of the test cases in each level will depend on their importance, for example, determine if the user login or not, is more important than what information is shown on the interface.

## Techniques and Tools

SeetGeek requires several techniques used for testing itself to ensure it is expected. Techniques the Group 66 will use in the future are security testing, usability testing, reliability testing, capability testing and regression testing. 

Security Testing is used to determine if the data and information that is used and stored are safe or not. 

Usability testing used to determine whether the frontend design fit the intended workflow for various comment require. Meanwhile, usability testing is used to ensure the program is intuitive to use which requires the program is easy to use from the user perspective. This technique also helps developers to review whether separate features are meet the required workflow no not, as does the system as a whole. 

Capability testing used to determine all of the separate functions, feature classes integrated by functions, and the system as a whole are meet required function. 

Regression testing used to determine the existing functionality is stable though code is changed, adding new code, or something else like fixing the bug. For regression testing, the tool, Github action will be used, every change of code will awake action to test.

In more detail, the Group 66 use requirement partitioning to partition the function specification into various small requirement and creat test case for each, such as separate sell session specification into `Command invalid if the user has not logged in`, `Starts a ticket selling session`, `Should ask four input (ticket name, price, quantity, date)`, etc,... Then, use a hybrid method and input boundary testing to create test cases for testing each function while the function needs input. 

The tool used for testing has been mention before, is Github action in automated. Meanwhile, manual inspection is also be used.


## Environments

Local: Windows, MacOS

IDLE environment: VSCode

Language: Python

Cloud: github



## Responsibility

   |                        Session Specification                         |  Contact Name                                               | Contact Information                                               |
 | :----------------------------------------------------------: | ------------------------------------------------------------ | ------------------------------------------------------------ |
 |  Landing   | Yixuan Fan  |     17YF20@queensu.ca           |
 |  Login   |   |                |
 |  Register   |   |                |
 |  Log Out   |   |                |
 |  Sell   | Qiru Jin  |     17qj@queensu.ca           |
 |  Buy   | Qiru Jin  |     17qj@queensu.ca           |
 |  Update   | Yixuan Fan |       17YF20@queensu.ca         |
 |  Exit   | Yixuan Fan |        17YF20@queensu.ca       |



## Budget Management

