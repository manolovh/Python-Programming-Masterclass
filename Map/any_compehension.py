from data import people, plants_dict, plants_list

# people = []
# if all([person[1] for person in people]) and bool(people):
if all([person[1] for person in people]) and people is True:
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == 'Grass' for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

# if any(['Grass' in plant for plant in plants_dict.values()]): # my solution
# if any([plant.plant_type == 'Grass' for plant in plants_dict.values()]): # Tim's solution
if any(plant.plant_type == 'Grass' for plant in plants_dict.values()):  # using a generator to save memory
    print("We found grass")                                             # by iterating over it and not creating a list
else:
    print("Nope, no grass here!")
