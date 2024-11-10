from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_size=get_next_size()
        if self.collision_type=="Chain":
            new_table=HashSet(self.collision_type, (self.params[0], new_size))
            for i in range(self.table_size):
                if self.table[i] is not None:
                    for j in range(len(self.table[i])):
                        new_table.insert(self.table[i][j])
        elif self.collision_type=="Linear":
            new_table=HashSet(self.collision_type, (self.params[0], new_size))
            for i in range(self.table_size):
                if self.table[i] is not None:
                    new_table.insert(self.table[i])
        else:
            new_table=HashSet(self.collision_type, (self.params[0], self.params[1], self.params[2], new_size))
            for i in range(self.table_size):
                if self.table[i] is not None:
                    new_table.insert(self.table[i])
        # self.table=new_table
        self.table = new_table.table
        self.table_size = new_table.table_size
        self.size=new_table.size
        if self.collision_type == "Double":
            self.params=(self.params[0], self.params[1], self.params[2], new_size)
        else:
            self.params=(self.params[0], new_size)
        pass
        
    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_size=get_next_size()
        if self.collision_type=="Chain":
            new_table=HashMap(self.collision_type, (self.params[0], new_size))
            for i in range(self.table_size):
                if self.table[i] is not None:
                    for j in range(len(self.table[i])):
                        new_table.insert(self.table[i][j])
        elif self.collision_type=="Linear":
            new_table=HashMap(self.collision_type, (self.params[0], new_size))
            for i in range(self.table_size):
                if self.table[i] is not None:
                    new_table.insert(self.table[i])
        else:
            new_table=HashMap(self.collision_type, (self.params[0], self.params[1], self.params[2], new_size))
            for i in range(self.table_size):
                if self.table[i] is not None:
                    new_table.insert(self.table[i])
        # self.table=new_table
        self.table = new_table.table
        self.table_size = new_table.table_size
        self.size=new_table.size
        if self.collision_type == "Double":
            self.params=(self.params[0], self.params[1], self.params[2], new_size)
        else:
            self.params=(self.params[0], new_size)
        pass
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
