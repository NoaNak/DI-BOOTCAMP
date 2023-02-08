# name: Zara
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
# France: blue, 
# Spain: red, 
# US: pink, green


brand = {"name: Zara", "creator_name: Amancio Ortega Gaona", "type_of_clothes: men, women, children, home", "international_competitors: Gap, H&M, Benetton","number_stores: 7000", "France: blue", "Spain: red", "US: pink, green"}

brand["number_stores"] = 2

sentence = f'the clients of zara are {brand["type_of_clothes"][0]} and {brand["type_of_clothes"][1]} and {brand["type_of_clothes"][2]}'
print(sentence)

brand['country_creation'] = 'Spain'

brand.get("international_competitors", None)

brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(brand["international_competitors"][-1])

print(brand["major_color"][-1]['US'])


print("Length of dictionary is",len(brand))

for key, value in brand.items():
    print(key)


more_on_zara = {

    'creation_date': 1975, 
    'number_stores': 10000,
}

all = brand.update(more_on_zara)

