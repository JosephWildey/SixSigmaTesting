import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


# load data for 1-Way ANOVA test on pg.
df = pd.read_csv('1WANOVA.csv')

# generate a boxplot to help detect outliers
plt.boxplot(df)

# display the boxplot
plt.show()

# get a statistical summary on the boxplot
print(df.describe())

# fairly standard alpha value
alpha = 0.05

print("Running Shaprio-Wilk tests...")

# use a Shapiro-Wilk test to test for normality
# Runs a separate test on each column
for columnName in df:
    stat, p = stats.shapiro(df[columnName])

    # nail down the problematic column giving us a low p-value
    print("p: {}\nalpha: {}".format(p, alpha))

    # Tell us if the column is a normal distribution
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')

print("Running K^2 tests...")

# Use a D'Agostino K^2 test to test for normality
for columnName in df:
    stat, p = stats.normaltest(df[columnName])

    # nail down the problematic column giving us a low p-value
    print("p: {}\nalpha: {}".format(p, alpha))

    # Tell us if the column is a normal distribution
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')


# calculate and output values from 1-Way Anova
# print(stats.f_oneway(df['Original Packaging'], df['Padded Envelope'], df['Packing Peanuts']))
