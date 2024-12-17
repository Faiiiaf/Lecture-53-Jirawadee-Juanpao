import csv

with open('friend.csv', mode='w') as csvfile:
    fieldnames = ['name','fav_movie','fav_pet']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name":"Faii","fav_movie":"Pulp Fiction","fav_pet":"Dog"})
    writer.writerow({"name": "Ploy", "fav_movie":"Nothing Hill", "fav_pet": "Cat"})
    writer.writerow({"name": "Pear", "fav_movie":"7sins", "fav_pet": "Cat"})

