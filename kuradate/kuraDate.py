from PIL import Image;


person1 = "Tom"
person2 = "Jerry"
restaurant = "Mammy Two Shoes"
feelings= ["bad","Angry","Annoyed","Great","Loving","Delighted"]

print("Welcome "+ person1 +" and " + person2 + " to the famous "+ restaurant +" Restaurant")
print("I hope you both are having a lovely afternoon. I have here the menu for you.")

budget = int(input("Can I know your budget for tonight, so i can recommend you our Fav main course ? $"))
print(budget)

foodOption = {"FISH DISH":["Tuna Tartar", "Salmon Sushi"], "CHEESE" : ["Mozarella","Jack Cheese", "Cheddar"], "Not Hungry": "None"}
print("Food Cooking in the Background .... !")

#print("Want to Play game in the mean time ? 1)Snake")
#execfile("snake.py")


print("Hello " + person1 + " What would you like as your main course?")
person1Food = input(foodOption)
person1FoodPrice = 50

tomImage = Image.open("tom-food.jpeg")
tomImage.show()

print("Hello " + person2 + " What would you like as your main course?")
person2Food = input(foodOption)
person2FoodPrice = 30

jerryImage = Image.open("jerryfood.gif")
jerryImage.show()

dateRating1 = int(input("Hello " + person1 + " what rating would you give from 1-5 ?"))
print(dateRating1)

dateRating2 = int(input("Hello " + person2 + " what rating would you give from 1-5 ?"))
print(dateRating2)

avgDateRating = (dateRating1 + dateRating2) / 2
avgDateRating = int(avgDateRating)

sum = person1FoodPrice + person2FoodPrice 
print("Your total charge for the food is $" + str(sum))

budget = budget - sum

print("You have $" + str(budget) + " remaining in your wallet")

if avgDateRating < 3 or person1Food == "None" or person2Food == "None":
    print("Thank you " + person2 + " but i dont like what you EAT !!")
else:
    print("The Food Was Awesome ! " + person1 + " Can we do this again sometime soon?")
