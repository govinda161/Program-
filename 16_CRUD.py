# Create a list of city names
city = ['Mumbai','Thane','Navi Mumbai','Delhi','Bangalore','Pune','Nashik','Varanasi']
print(city)
print(city[0:3])

#Update
city.append('Kanpur')
print(city)

city.insert(8,'Bhopal')
print(city)

#Delete
city.pop(9)
print(city)

city.remove('Bhopal')
print(city)
