#ex1
# Access the value of key "history"

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}


#ex2
# Delete set of keys from Python Dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    del sample_dict[key]

print(sample_dict)

# je peux faire aussi:

# del sample_dict["salary"]
# del sample_dict["name"]
# print(sample_dict)