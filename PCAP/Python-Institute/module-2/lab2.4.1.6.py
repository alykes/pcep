def configure_led(number_string):
    final_result = []
    row_list = []
    row_string = ""

    for row in range(len(lst[0])):
        for x in number_string:
            row_list.append(row_string + lst[int(x)][row])
            
        final_result.append(row_list)
        row_list = []
            
    # Return the list
    return final_result

#    
# Main program starts here
#     
lst = [["###", "# #", "# #", "# #", "###"], 
       ["  #", "  #", "  #", "  #", "  #"],
       ["###", "  #", "###", "#  ", "###"],
       ["###", "  #", "###", "  #", "###"],
       ["# #", "# #", "###", "  #", "  #"],
       ["###", "#  ", "###", "  #", "###"],
       ["###", "#  ", "###", "# #", "###"],
       ["###", "  #", "  #", "  #", "  #"],
       ["###", "# #", "###", "# #", "###"],
       ["###", "# #", "###", "  #", "###"]]


num = input("Please type a number you would like to display: ")

# Just a bit of input validation here
if num.isdigit():
    # Call the Function to configure the LED Display
    display_config = configure_led(num)
    
    # Print the number
    for re in range(len(display_config)):
            print(" ".join(display_config[re]))

else:
     print("Please enter an integer value!")

