failure report in clear table form, listing test name or number, what was being tested, the nature of the failure, what the error in the code was, and what actions were taken to fix it

| Test Name        | Purpose                                                                                             | Failure                                      | Error in the code                                      | How Fix                                                        | Failures addressed or not |
|-----------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------|--------------------------------------------------------|----------------------------------------------------------------|---------------------------|
| test_b_2 | Check the updated account file and ticket file is correct content | actual balance not matching expected balance | ticket cost is pure price, not calculate the tax and service fee | add a correct variable named cost | Addressed                 |
| test_b_2 | Check the updated account file and ticket file is correct content | actual balance not matching expected balance | ticket cost should be int but not float                      | transform the float into int      | Addressed                 |


