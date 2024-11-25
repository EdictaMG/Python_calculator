#need a variable and base value on which to add numbers
total = 0

#calculation will continue adding to the variable "total" ("while True") until addition ('add') is called ("break")
#status of total (based on the numbers added to it) will be converted into a "float" data type before printing the total sum

while True:
    print("Enter a number or write 'add' to sum all previous inputs.")
    user_input = input()  # user_input is the input provided by user
    if user_input == "add":  # compare user's input to 'add'
        break # if the user's input is 'add', then break the code
    else:
        total+=float(user_input)
print(total)
