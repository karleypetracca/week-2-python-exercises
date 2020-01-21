# Exercise that works with existing Person class, and creates Vehicle class


# Person class

class Person:

    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.greeting_count = 0
         self.unique_people_greeted = []

    def __str__(self):
        return "Person: {} {} {}".format(self.name, self.email, self.phone)

    def greet(self, other_person):
         print('Hello {}, I am {}!'.format(other_person.name, self.name))
         self.greeting_count += 1
         if other_person.name not in self.unique_people_greeted:
            self.unique_people_greeted.append(other_person.name)

    def print_contact_info(self):
        print("{name}'s email: {email}, {name}'s phone number: {phone}".format(name = self.name, email=self.email, phone=self.phone))
    
    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return len(self.friends)

    def num_unique_people_greeted(self):
        return "Unique people greeted: {}".format(len(self.unique_people_greeted))

        


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
dee_ann = Person("Dee Ann", "deeann@gmail.com", "496-889-5600")

sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.num_unique_people_greeted())

print(sonny.email, " ", sonny.phone)
print(jordan.email, " ", jordan.phone)

sonny.print_contact_info()

sonny.add_friend(jordan)
print(sonny.friends)
print(sonny.num_friends()) # Shows number of friends

sonny.greet(jordan)
print(sonny.num_unique_people_greeted())
print(sonny.greeting_count) # Shows greeting count

print(sonny) # Prints __str__ attribute from Person class

print(sonny.num_unique_people_greeted()) # Prints number of unique people greeted
sonny.greet(dee_ann)
print(sonny.num_unique_people_greeted())



# Vehicle class

class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(self.year, self.make, self.model)


