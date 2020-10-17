## Testing Framework
The chosen testing framework, pytest, which can be activated by the CI/CD pipeline once a pull activity is being requested. The testing workflows can be configured inside GitHub Actions. Multiple workflows can be set up here to test each unit, module, or frontend feature. When a pull request, GitHub Actions will give the tester a warning; also, the pulling process will be paused until all the pytest checks are completed and passed. If any test failed, the tester could see a detailed report on the Checks page under Pull Requests to find the location of the bug or the reason why the testing failed. Once all the checks are marked pass, the tester can then complete the merging activity.

##The way to organize Different Test Case file


First, we will have a folder for all the Test cases, and then we have a sub-folder for specification Sections, for example, we will have Landing, login, Buy&Sell.
The name of test case code files will have a very organized file name: The test ID from test case plan+Test section. For example, as “R31.11_Login”
（bellowing is optional）
Moreover, if sometimes we need to search for a specific test case (as the non-numerical input negative case for Ticket information test), we might create a multi-dimensional array to store different test cases and its description. As each element in the array would be [“Test_Case_Section”, “Specific Description”, “filename”] for us to find the specific test case filename.
