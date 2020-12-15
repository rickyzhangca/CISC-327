During the integration between frontend end backend, multiple conflicts has been expirenced, and most of them were related to directories. The team utilized numbers of methods to resolved the conflicts faced. The table below illustrated the problem and solution for each defect case.
|Problem|Discription|Solution|
|-----------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------|
|Data directory|The original data folder dirctory selected during the frontend development was not accessable to the backend|Data has been moved outside the frontend directory|
|Empty copied files|The transaction files copied to the weekly data storage are empty, which was caused by the command sequence in the bash script was incorrect.|Forward the weekly transaction files saving command to the place before the backend runs.|
|Empty copied files|The transaction files copied to the daily data storage are empty, which was caused by the command sequence in the bash script was incorrect.|Forward the daily transaction files saving command to the place before the backend runs.|
|Unexpected File Status|The file after testing dosen't have the expected result. Since the testing was performed on file based on data, and it didn't clear out after the testing.|Clear out the transaction files in multiple tests|
|Data directory|Directory not found.No such file or directory: 'Kingston_transaction.csv',...|Type name error, change 'K' to 'k'| 
