# Test Plan

## Document Organization


The test cases are organized in the dedicated `./a1` folder in the following structure. `./qa327_test` is reserved for executeable codes only to prevent confusion. The last section talks about the planned organization of these code files.

```
|-- ...
|-- a1
    |-- testplan.md
    |-- test_cases
        |-- buy.md
        |-- exit.md
        |-- landing.md
        |-- login.md
        |-- logout.md
        |-- register.md
        |-- sell.md
        |-- update.md
```

In the folder, `testplan.md` explains the organziation of tests cases and how the team plans to run the tests. `test_cases` consists of the test cases in natural language. 

Instead of composing everything into one document or letting each team member claim their own folder, the team created files by transaction. It enables eaiser task splitting ([#5](https://github.com/rickyzhangca/CISC-327/issues/5)) and reduces optential merge conflicts.

## Testing Framework
The chosen testing framework, pytest, which can be activated by the CI/CD pipeline once a pull activity is being requested. The testing workflows can be configured inside GitHub Actions. Multiple workflows can be set up here to test each unit, module, or frontend feature. When a pull request, GitHub Actions will give the tester a warning; also, the pulling process will be paused until all the pytest checks are completed and passed. If any test failed, the tester could see a detailed report on the Checks page under Pull Requests to find the location of the bug or the reason why the testing failed. Once all the checks are marked pass, the tester can then complete the merging activity.

## The way to organize Different Test Case file
First, the team will create a folder for all the test cases, and then a sub-folder for specification Sections will be created, for example, Landing, login, Buy&Sell.
The name of test case code files will have a very organized file name: the test ID from the test case plan+Test section. For example, as “R31.11_Login”
（bellowing is optional）
Moreover, if sometimes the team need to search for a specific test case (as the non-numerical input negative case for Ticket information test), we might create a multi-dimensional array to store different test cases and its description. As each element in the array would be [“Test_Case_Section”, “Specific Description”, “filename”] for us to find the specific test case filename.
