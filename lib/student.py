#!/usr/bin/env python
# pytest lib/testing/student_test.py 
import ipdb

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = list()
    
    def learn(self,knowledge):
        if type(knowledge) == str:
            self.knowledge.append(knowledge)