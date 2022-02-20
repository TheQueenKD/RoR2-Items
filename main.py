"""
User input for what item they want to know more about
print the description of that item

example:
Pick an item:   Hopoo Feather
Hopoo Feather: Gives one extra jump

layout:
Get user input for which item they want from the dict
make the input all lower case
print item name and description
"""


from functions import print_item_list_or_description


item_choice = input('Pick an item! Hit enter for item list!\t').title()
print()  # separating inputs from outputs
print_item_list_or_description(item_choice)
