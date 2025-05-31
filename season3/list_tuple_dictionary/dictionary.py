# dictionary

d = {"Tom": 77799184,"Jerry": 77799185, "Spike": 77799186, "Tyke": 77799187}

print(d)

# print(d["tom"])

# add a new entry in this phone book

d["sam"] = 77799188

print(d)

# delete an entry in this phone book

del d["Jerry"]

print(d)

# print all the directory values

for key in d:
      print("key", key, "value:", d[key])


for k, v in d.items():
    print("key", k, "value:", v)


# check if a specific persons name is there in the phone book or not

if "Tom" in d:
      print("Tom is in the phone book")
else:
      print("Tom is not in the phone book")

# d.clear

# print(d)
