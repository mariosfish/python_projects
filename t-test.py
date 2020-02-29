# Perform F-test for every feature
alpha = 0.025
for col in df.columns[:-1]:
    F = np.var(df[col]) / np.var(df['sharknado hazard'])
    df1 = len(df[col]) - 1
    df2 = len(df['sharknado hazard']) - 1
    p_value = stats.f.cdf(F, df1, df2)
    if p_value > alpha:
        print(
            f"The column {col} is not related with the column 'sharknado hazard'.")
    else:
        print(
            f"-->The column {col} is related with the column 'sharknado hazard'.<--")


# function for calculating the t-test for two independent samples
def independent_ttest(data1, data2, alpha):
    # calculate means
    mean1, mean2 = np.mean(data1), np.mean(data2)
    # calculate standard errors
    se1, se2 = stats.sem(data1), stats.sem(data2)
    # standard error on the difference between the samples
    sed = np.sqrt(se1**2.0 + se2**2.0)
    # calculate the t statistic
    t_stat = (mean1 - mean2) / sed
    # degrees of freedom
    df = len(data1) + len(data2) - 2
    # calculate the critical value
    cv = stats.t.ppf(1.0 - alpha, df)
    # calculate the p-value
    p = (1.0 - stats.t.cdf(abs(t_stat), df)) * 2.0
    # return everything
    return t_stat, df, cv, p


alpha = 0.05

for col in df.columns[:-1]:
    t_stat, dfs, cv, p = independent_ttest(
        df[col], df['sharknado hazard'], 0.025)
    print('t=%.3f, dfs=%d, cv=%.3f, p=%.3f' % (t_stat, dfs, cv, p))
    # interpret via critical value
    if abs(t_stat) <= cv:
        print(
            f'Column: {col} - sharknado hazard: Accept null hypothesis that the means are equal.')
    else:
        print(
            f'Column: {col} - sharknado hazard: Reject the null hypothesis that the means are equal.')
    # interpret via p-value
    if p > alpha:
        print(
            f'Column: {col} - sharknado hazard: Accept null hypothesis that the means are equal.\n')
    else:
        print(
            f'Column: {col} - sharknado hazard: Reject the null hypothesis that the means are equal.\n')
