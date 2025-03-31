# add your Student class here!
class Student:
    def __init__(self, name, class_year, classes):
        self.name = name
        self.class_year = class_year
        self.classes = classes
        self.num_classes = len(classes)

    def add_class(self, class_name):
        '''
            This function has 2 paramenters. The first argument helps
            us access all attributes(i.e. name, classes) in the constructor.
            It should append the second argument, in this case it's called class, to the self.classes list
        '''
        self.classes.append(class_name)

    def get_num_classes(self):
        '''
            This function has 1 paramenter. It helps us access all attributes(i.e. num_classes) 
            in the constructor. It should return the value of self.num_classes
        '''
        return self.num_classes
    
    def summary(self):
        '''
            This function has 1 paramenter. It helps us access all attributes(i.e. name, class_year) 
            in the constructor. It should return a string => example f"Samara is a junior enrolled in 7 classes"
        '''
        return self.summary (f"{self.name} is a {self.class_year} enrolled in {self.num_classes} classes")