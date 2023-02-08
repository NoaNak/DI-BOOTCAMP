# Write a function called describe_city() that accepts the name of a city and its country as parameters.

def describe_city(city, country = "France"):
    print(f"{city} is in {country}")
    print(describe_city)

describe_city("paris")


# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.