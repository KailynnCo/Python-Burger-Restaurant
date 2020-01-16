import operator #libabry gives you functions
def lists(): #define a function
    count = 0
    customersname = [] #emtpy list
    time = [0,0,0,0,0,0,0,0,0,0,0,0] #10am -9pm  military: 10 - 21 open 12 hours
    timeProfit = [0,0,0,0,0,0,0,0,0,0,0,0] #10am -9pm  military: 10 - 21 open 12 hours #another one so we can have a place for the index
    burgername = [] #emtpy list
    burgercost = [] #emtpy list
    temp = 0 #emtpy list
    print("Are you a new customer Y or N")
    userInput = input(" ").lower() #.lower is to make all characters lower case
    while userInput == "y" and count <= 100: #may no be over 100 clients
        print("What is the customers name?")
        customersname.append(input("Name: ").lower()) #.append to add input to the list
        print("What is the time of day? Use military") 
        tempTime = int(input("Time: ")) 
        if tempTime > 9 and tempTime < 22: # makes sure the time entered is within 10am to 9 pm
          time[tempTime - 10] += 1 #its -10 because the we are using military, since its a time sale from 10-21 but we want to make 10 0 to make it a easy refrecne 
        print ("What is the burger name?")
        tempBurger = input("Burger: ").lower() #temp burger because the if statement is not calling  an array, its calling a string 
        burgername.append(tempBurger)
        if tempBurger == "cheese":
            burgercost.append(12)
            timeProfit[tempTime - 10] += 12 #temptime -10 cause we want it to equal to 0 and we add 12 which is the burger cost 
        elif tempBurger == "hamburger":
            burgercost.append(10)
            timeProfit[tempTime - 10] += 10
        elif tempBurger == "bacon":
            burgercost.append(9)
            timeProfit[tempTime - 10] += 9
        elif tempBurger == "double":
            burgercost.append(15)
            timeProfit[tempTime - 10] += 15
        elif tempBurger == "jalapeno":
            burgercost.append(8)
            timeProfit[tempTime - 10] += 8
        elif tempBurger == "impossible":
            burgercost.append(14)
            timeProfit[tempTime - 10] += 14
        count += 1 #count = count + 1
        print("Are you a new customer Y or N")
        userInput = input(" ").lower()
    return customersname, time, burgername, burgercost, timeProfit #return
def topthreeburger(burgers):
    countc = 0
    counth = 0
    countb = 0
    countd = 0
    countj = 0
    counti = 0
    grandtotal = 0
    for i in range(len(burgers)):
        if burgers[i] == "cheese":
            countc += 1 #add +1 for a loop,every time someone order a chesse it while add up
        elif burgers[i] == "hamburger":
            counth += 1
        elif burgers[i] == "bacon":
            countb += 1
        elif burgers[i] == "double":
            countd += 1
        elif burgers[i] == "jalapeno":
            countj += 1
        elif burgers[i] == "impossible":
            counti += 1
    grandtotal += (12 * countc) + (10 * counth) + (9 * countb) + (15 * countd) + (8 * countj) + (14 * counti) #for grantal toal we have to multiple by the cost then add those for the grandtotal
    burgernamelist = ["cheese", "hamburger", "bacon", "double", "jalapeno", "impossible"]  
    total_burgers = [countc, counth, countb, countd, countj, counti] #these are the total burgers
    return burgernamelist, total_burgers, grandtotal #return statements
def main(): 
    customersname, time, burgername, burgercost, timeProfit = lists()
    burgernamelist, total_burgers, grandtotal = topthreeburger(burgername) #creating varaiables within the scope of the main function and grabbing from the list function
    #1 Name of the client number 3
    print ("Client number 3 is:", customersname[2])
    #2 The client with the longest name
    longestname = max(customersname, key=len) #key is the function to sort by the length 
    print("The longest name is:", longestname)
    #3 Top three most selling burgers
    print (burgernamelist, total_burgers) #import function
    topburgernumber = int(input("Enter the position of highest number: ")) -1
    topsecburgernumber = int(input("Enter the position of the second highest number: ")) -1
    topthirdburgernumber = int(input("Enter the position of the third highest number: ")) -1
    print ("Top three burgers are: ", burgernamelist[topburgernumber], burgernamelist[topsecburgernumber], burgernamelist[topthirdburgernumber]) 
    #6 Busiest hour of the day
    index, value = max(enumerate(time), key=operator.itemgetter(1)) # uses operator library it finds largest number in an array and returns its location(index). maxenumerate:(timeprfoit) is going to locate biggest postion of max.
    print ("The busiest hour of the day was at", index + 10, " with ",value, " clients") #itemgetter: is a function that returns a function, which will return an indexedses operator library it finds largest number in an array and returns its location(index)
    #7 Best hour of the day
    indexp, valuep = max(enumerate(timeProfit), key=operator.itemgetter(1)) # uses operator library it finds largest number in an array and returns its location. index is  valuep (using time profit array)
    print ("Most money made at time ", indexp + 10, " was $",valuep)
    #8 Total sales on the day
    print ("The total sales of the day were $",grandtotal) #adds the grand totals from up above
main() #calling main


