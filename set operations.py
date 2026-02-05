friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print("common interests between both friends: ",friend_a & friend_b)
print("All interests of both individuals:",friend_a | friend_b)
print("Interests of friend A that B doesnt have:",friend_a - friend_b)