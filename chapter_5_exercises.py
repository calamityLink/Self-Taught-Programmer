print("Exercise 1")

fav_music = ["Mighty Mighty Bosstones", "MCR", "Fallout Boy"]
print(fav_music)


print("Exercise 2")

places_visited = [(40.25,75.65),(51.51,0.13),(19.64,156.00)]
print(places_visited)


print("Exercise 3,4")

details = {"Height":"6'1",
           "Favorite Color":"Green",
           "Favorite Author":"Garth Nix"}

ask = input("Would you like to know my Height, Favorite Color, or Favorite Author? ")
if ask in details:
    print("Thanks for asking! My " + ask + " is " + details[ask] + ".")
else:
    print("Invalid entry")


print("Exercise 5")

fav_music = {"Mighty Mighty Bosstones":["Impression","They Came to Boston"],
             "MCR":["Na Na Na","Helena"],
             "Fallout Boy":["Centuries","I Don't Know"]}
print(fav_music)

