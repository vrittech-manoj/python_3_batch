name = "kathmandu"

# for letter in name: 
#     full_letter = "@"+letter  
#     print(full_letter)


# WAP to display below format output
#  it is an apple 
#  it is a ball 
#        a cat 
#       a dot
        # an elephant
first_data = ['apple','ball','cat','dog','elephant'] #list 
for item in first_data:
    if item[0] in 'aeiou':
        output = "an"
    else:
        output = "a" 
    sentence = "it is " + output + " " + item
    print(sentence)

