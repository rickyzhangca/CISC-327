# CISC 327 A2 - Detailed Test Plan

## Organization 

The current program is the SeetGeek online Customer-to-Customer ticket selling system, that Group 66 should make a test case structure for it. The main idea of SeetGeek is supporting to a registered user who can buy and sell tickets through this online application. Two components make the user interacts with the system through the terminal, a front-end component, and a backend component. Each component will be put to different new classifiers, 'frontend' and ‘backend' because each of them is a standalone program. Each classifier is a category include a whole range of feature fits in. Take the 'frontend' for example, landing, login, register, buy, sell, and the update should be put under frontend because all of them refer to the same purpose-supporting program interact with the user. So does the backend component. Then, various functions made up a feature, so this invites a new degree of separation. Finally, create sufficient unit test cases for each function, then create sufficient integration test cases for each feature, and two components at the end.
then introduces a new degree of separation: grouped by feature-wise [different classes] ->[each smaller function in classes]
Corresponding integration testing

## Order

Start first at unit testing to verifies every single function meet the detailed design specification; secondly, integration testing verifies that the group of units can be integrated and work, also need to meet the design specification; thirdly, complete program be verifies that meet the functional specification by system testing; finally, acceptance testing validates program that accepts by customer. 
Unit testing -> integration testing -> system -> acceptance

## Techniques and Tools

SeetGeek requires several techniques used for testing itself to ensure it is expected. Techniques the Group 66 will use in the future are security testing, usability testing, reliability testing, capability testing and regression testing. Security Testing is used to determine if the data and information that is used and stored are safe or not. Usability testing used to determine whether the frontend design fit the intended workflow for various comment require. Meanwhile, usability testing is used to ensure the program is intuitive to use which requires the program is easy to use from the user perspective. This technique also helps developers to review whether separate features are meet the required workflow no not, as does the system as a whole. Capability testing used to determine all of the separate functions, feature classes integrated by functions, and the system as a whole are meet required function. Regression testing used to determine the existing functionality is stable though code is changed, adding new code, or something else like fixing the bug.


tool: action - Pytest

Unit testing: Pytest? #Try Expect? Wrapup? Mocks?

Integration testing: Wrapup 


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
 |  Sell   |   |                |
 |  Buy   |   |                |
 |  Update   |   |                |
 |  Exit   | Yixuan Fan |        17YF20@queensu.ca       |



## Budget Management

