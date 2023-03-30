'Python' == 'Python'    # True

'Python' == 'python'    # False

'Python' == 'Pytho'     # False

'Python' != 'python'    # True

# Python checks the code point when performing < and > comparisons
# Python searches for the first differing character and checks them against one another

'I love Python!' < 'I love python!' # True - ord('P') = 80 and ord('p') = 112
'I love Pyth' < 'I love Python!'    # True - because it is identical but contains less characters
'A' < 'So, what do you reckon?'     # True - because A has a smaller code point than S
'So what' < 'Art is cool!'          # False - because S has a larger code point than A
'8' < '20'                          # False - Python looks at the code point then compares the values ord('8') = 56 and ord('2') = 50

'I love Python!' > 'I love python!'             # False - ord('P') = 80 and ord('p') = 112
'I love Python! Malaka!' > 'I love Python!'     # True - because it is identical but contains more characters



# Note
'10' == 10  # False - always will be False
'10' != 10  # True
80 == 'P'   # False
# If you use any other operators, it will cause a TypeError because of 'str' and 'int'