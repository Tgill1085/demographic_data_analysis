import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # select the column of 'race' in the data frame to get counts of each
    race_count = df['race'].value_counts()

    # What is the average age of men?
    # select the sex and age in data frame, then avg
    average_age_men = df[df["sex"] == "Male"]["age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    # first find the total number of people with Bachelors under education
    totalbach = len(df[df["education"] == "Bachelors"])
    # to calculate percentage, find the total number of people
    totalpeople = len(df)
    # calculate percentage by dividing the bachelors by total people
    percentage_bachelors = round(totalbach / totalpeople *100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # select just the higher education values in column
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    # from the higher education, find the total people who earn more than 50K
    highedhighsal = len(higher_education[higher_education.salary == ">50K"])

    # select just the lower education values in the column by excluding the higher education values.
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    # from the lower education, find the total people who earn more than 50K
    lowedhighsal = len(lower_education[lower_education.salary == ">50K"])

    # percentage with salary >50K
    # for both percentages, take the totals of each category, and divide by total educated
    higher_education_rich = round(highedhighsal / len(higher_education) * 100, 1)
    lower_education_rich = round(lowedhighsal / len(lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    # select the hours-per-week column, and apply minimum function
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # select the rows that match the minimum hours worked per week
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    # calculate the percentage by selecting the total number of workers who work the minimum hours and make over 50K, and dividing this by selecting the total number of workers who work the minimum hours. 
    rich_percentage = round(len(num_min_workers[num_min_workers.salary == ">50K"]) / len(num_min_workers) *100, 1)

    # What country has the highest percentage of people that earn >50K?

    # first, find the amount of countries listed in "native-country"
    countrytotal = df['native-country'].value_counts()
    # next, select the rows that show earnings over 50K
    countryhighsal = df[df['salary'] == '>50K']['native-country'].value_counts()
  
    # return the country with the highest number of high salary earners, using index max function
    highest_earning_country = (countryhighsal / countrytotal *100).idxmax()
    # return the highest percentage of high salary earners in the highest earning country
    highest_earning_country_percentage = round((countryhighsal / countrytotal *100).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    # select workers from India, who make more than 50K
    indiahighsal = df[(df['native-country'] == "India") & (df['salary'] == ">50K")]
    # calculate the total number of occupations being reported
    indiaocc = indiahighsal['occupation'].value_counts()
    # return the index of the maximum occurances of occupations from the high earners
    top_IN_occupation = indiaocc.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
