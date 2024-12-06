#A dictionary containing an employee details:
employee1 = {
  "name": "Ram",
  "age": 25,
  "location": "Delhi"
}

print(employee1)

#Add a new field named "job"
employee1["job"] = "Manager"
print(employee1)

#update the age field
employee1["age"] = 28
print(employee1)

#remove the location key
employee1.pop("location")
print(employee1)

#accessing a key which does not exists
print(employee1["salary"])