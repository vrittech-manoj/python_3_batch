first_name = "ram"
second_name =  "shyam"

print(first_name+second_name) #concat

a = "ram"
b = 9
print(a+str(b))

first_sentence = "    hello i am from mars   "

print(first_sentence.strip())

skill_shikshya = "skillshikshya@gmail.com"

splitted_data = skill_shikshya.split('@') 
print(splitted_data)#['skillshikshya', 'gmail.com']


about_nepal = "nepal is ....nepal .. kahsiudqe alasdkdlkqpqoei india ... iasjd .. india"
corrected_data = about_nepal.replace('india','nepal') #replace is used to replace old to new value
corrected_data = corrected_data.replace('.','the')
print(corrected_data)

father_name = "some name"
print(father_name.upper())
print(father_name.capitalize())
print(father_name.title())
#class work , describe any 10 string manipulation function with example.

data = "hello world how are you"
splitted_data = data.split(' ')
print(splitted_data)
joined_data = ','.join(splitted_data)
print(joined_data)

