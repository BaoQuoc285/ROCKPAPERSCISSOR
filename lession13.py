person = "bao"
coins = 3
#cach 1 
print( "\n" + person + " has " + str(coins) + " coins left.")
#cach 2
mes = "\n%s has %s coins left." %(person,coins)
print(mes)
#cach 3 
mes1 = "\n{} has {} coins left." .format(person,coins)
print(mes1)

# CACH 3 CON CO THE DINH DANG DC VI TRI 
mes2 = "\n{1} has {0} coins left." .format(coins,person)
print(mes2)
#cach khac
mes3 = "\n{person} has {coins} coins left." .format(coins = coins,person = person)
print(mes3)
# CO THE DUA NO VAO DICT
dict = {
    'coins' : coins,
    'person': person
}
mes4 = "\n{person} has {coins} coins left." .format(**dict)
print(mes4)

##########################

#fstring 
message = f"\n{person} give me {coins} coins left."
print(message)

message2 = f"\n{person} give me {2 * 8} coins left."
print(message2)