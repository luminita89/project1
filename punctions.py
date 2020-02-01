# ## defining the function
# def greet_user(name, lastName):
#     """Function to greet the user."""
#     # print ('HELLO!')
#     return (f'Hello,{name} {lastName}!')


# ##calling the functions
# ## greet_user()
# print(greet_user('John', 'Lee'))
# msg = greet_user('John', 'Lee')
# print (msg)

# # keywords (default) arguments 
# def greet_user_kwd(name, lastName)
#  """Function to greet the user with name."""
#  return (f'Hello, {name} {lastName}')

#  print (def greet_kwd('John'))
#   print (def greet_kwd('John', lastName='Lee'))

#   def triangle_area(height=0, base=0):
#         return(height) *base * 0.5

# print(triangle_area(4, 5)) 

def describe_city(city, country='usa') :
  """return the message with the city and country"""
  return(f'{city.tittle()}, is in{country.upper()}')
print(describe_city("chicago"))
print(secribe_city("paris", "france"))

def remove_duplicate(anylist):
    return set (anylist)
    
