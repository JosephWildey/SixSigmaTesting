# OneWay.Py (1-Way ANOVA)
This script performs a 1-Way ANOVA test, with mostly appropriate checks in place. You can specify a csv file that will be read into a Pandas dataframe. 
From there, you will get a boxplot and summary of the dataframe. This lets you eyeball the dataset before you dive too deep into analysis.
Then once you close the boxplot a Shapiro-Wilk and D'Agnostino K^2 test is run on each column of the dataset. For each iteration of each test.
it will compare the p value of the test to your alpha value, and then determine whether to reject the null hypothesis. 
Once all that has concluded, it will run a 1-Way ANOVA test and return the f-value and p-value. It does not perform a check at this level.

I wrote this script quickly. and if I have time I will improve its functionality.
