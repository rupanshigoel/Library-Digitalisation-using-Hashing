from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.collision_type=collision_type
        self.params=params
        self.size=0
        if collision_type == "Chain":
            self.table=[None]*params[1]
            self.table_size=params[1]
        elif collision_type == "Linear":
            self.table=[None]*params[1]
            self.table_size=params[1]
        else:
            self.table=[None]*params[3]
            self.table_size=params[3]
        pass

    
    def assign_val(self, letter):
        if 'a' <= letter <= 'z':  # Lowercase letters
            return ord(letter) - ord('a')
        else:
            return ord(letter) - ord('A') + 26
        
    def hash_fun_1(self, key, z):#giving z and not the parameter
        result=self.assign_val(key[-1])
        for char in key[-2::-1]:
            curr=self.assign_val(char)
            result=result*z + curr
        #not used mod abhi tak
        return result
    
    #change required for hash function 2, *2, *3,....
    def hash_fun_2(self, key, param):
        #z1,z2,c2,table_Size
        result=self.assign_val(key[-1])
        for char in key[-2::-1]:
            curr=self.assign_val(char)
            result=result*param[1] + curr
        result=result%param[2]
        # first=self.hash_fun_1(key, param[0])
        return (param[2]-(result%param[2])) # does not return final answer as compared to first function

    def insert(self, x):
        pass
    
    def find(self, key):
        pass
    
    def get_slot(self, key):
        pass
    
    def get_load(self):
        pass
    
    def __str__(self):
        pass
    

    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        pass
    
    def list_of_words(self):
        word_list=[]
        if self.collision_type=="Chain":
            for i in range(self.table_size):
                # word_list.extend(self.table[i])
                if self.table[i] is not None:
                    for j in range(len(self.table[i])):
                        word_list.append(self.table[i][j])
        else:
            for i in range(self.table_size):
                if self.table[i] is not None:
                    word_list.append(self.table[i])
        return word_list

    def insert(self, key): 
        if self.collision_type == "Chain":
            new=self.get_slot(key)
            if self.table[new] is None:
                new_list=[]
                new_list.append(key)
                self.size+=1
                self.table[new]=new_list
            else:
                for i in range(len(self.table[new])):
                    if self.table[new][i]==key:
                        return 
                
                self.table[new].append(key)
                self.size+=1
        elif self.collision_type == "Linear":
            new=self.get_slot(key)
            c=0
            while self.table[new] is not None:
                if c>=self.table_size:
                    return
                c+=1
                if self.table[new] == key:
                    return
                new=(new+1)%self.table_size
                
            to_be_used=new
            self.table[to_be_used]=key
            self.size+=1
        else:
            new=self.get_slot(key)
            for i in range(self.table_size):
                index=(new + (i * super().hash_fun_2(key, self.params)))%self.table_size
                if self.table[index]==None:
                    self.table[index]=key
                    self.size+=1
                    return
                if self.table[index]==key:
                    return
            return

        pass
    
    def find(self, key):
        if self.collision_type == "Chain":
            new=self.get_slot(key)
            if self.table[new] is not None:
                for i in range(len(self.table[new])):
                    if self.table[new][i]==key:
                        return True
            return False
        elif self.collision_type == "Linear":
            new=self.get_slot(key)
            c=0
            while(self.table[new] is not None):
                if c>=self.table_size:
                    return False
                c+=1
                if self.table[new]==key:
                    return True
                new=(new+1)%self.table_size
            return False
        else:
            new=self.get_slot(key)
            for i in range(self.table_size):
                index=(new + (i * super().hash_fun_2(key, self.params)))%self.table_size
                if self.table[index]==None:
                    return False
                if self.table[index]==key:
                    return True
            return False
        pass
    
    def get_slot(self, key):
        return super().hash_fun_1(key, self.params[0])%self.table_size
        pass
    
    def get_load(self):
        return self.size/self.table_size
        pass
    
    def __str__(self):
        # if self.collision_type is "Chain":
        #     final_print=[]
        #     for i in range(self.table_size):
        #         for j in range(len(self.table[i])):
        string=""
        if self.collision_type=="Chain":
            for i in range(self.table_size):
                if self.table[i] is None:
                    string+="<EMPTY> "
                else:
                    for j in range(len(self.table[i])):
                        string+=self.table[i][j]
                        if j is not len(self.table[i])-1:
                            string+=" "
                            string+="; "
                if i is not self.table_size-1:
                    string+=" |"
        else:
            for i in range(self.table_size):
                if self.table[i]==None:
                    string+="<EMPTY> "
                else:
                    string+=self.table[i]
                if i is not self.table_size-1:
                    string+=" |"
        return string
        pass
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        pass
    
    def insert(self, x):
        # x = (key, value)
        if self.collision_type == "Chain":
            # print("a")
            new=self.get_slot(x[0])
            if self.table[new] is None:
                # new_list=[]
                # new_list.append((x[0], x[1]))
                # self.size+=1
                # self.table[new]=new_list
                self.table[new]=[]
                self.table[new].append((x[0], x[1]))
                # print(self.table[new][1])
                self.size+=1
            else:
                # print("b")
                for i in range(len(self.table[new])):
                    if self.table[new][i][0]==x[0]:
                        return 
                self.size+=1
                self.table[new].append((x[0], x[1]))
                # print(self.table[new][1])
        elif self.collision_type == "Linear":
            # print("b")
            new=self.get_slot(x[0])
            c=0
            while self.table[new] is not None:
                if c>=self.table_size:
                    return
                c+=1
                if self.table[new][0] == x[0]:
                    return
                new=(new+1)%self.table_size
                
            to_be_used=new
            self.table[to_be_used]=(x[0], x[1])
            # print(self.table[to_be_used][1])
            self.size+=1
        else:
            # print("c")
            new=self.get_slot(x[0])
            for i in range(self.table_size):
                index=(new + (i * super().hash_fun_2(x[0], self.params)))%self.table_size
                if self.table[index]==None:
                    self.table[index]=(x[0], x[1])
                    # print(self.table[index][1])
                    self.size+=1
                    return
                if self.table[index][0]==x[0]:
                    return
            return
        pass
    
    def find(self, key):
        if self.collision_type == "Chain":
            new=self.get_slot(key)
            if self.table[new] is not None:
                for i in range(len(self.table[new])):
                    if self.table[new][i][0]==key:
                        return self.table[new][i][1]
            return None
        elif self.collision_type == "Linear":
            new=self.get_slot(key)
            c=0
            while(self.table[new] is not None):
                if c>=self.table_size:
                    return None
                c+=1
                if self.table[new][0]==key:
                    return self.table[new][1]
                new=(new+1)%self.table_size
            return None
        else:
            new=self.get_slot(key)
            for i in range(self.table_size):
                index=(new + (i * super().hash_fun_2(key, self.params)))%self.table_size
                if self.table[index]==None:
                    return None
                if self.table[index][0]==key:
                    return self.table[index][1]
            return None
        pass
    
    def find_keyword(self, keyword):
        book_list_key=[]
        if self.collision_type=="Double":
            for i in range(self.params[3]):
                # print(self.table[i])
                if self.table[i] is not None:
                    
                    if self.table[i][1].find(keyword):
                        book_list_key.append(self.table[i][0])
        elif self.collision_type=="Linear":
            for i in range(self.params[1]):
                
                if self.table[i] is not None:
                    # print(self.table[i][1])
                    # print(self.table[i])
                    if self.table[i][1].find(keyword):
                        book_list_key.append(self.table[i][0])
        else:
            for i in range(self.params[1]):
                
                if self.table[i] is not None:
                    # print(self.table[i][1])
                    # print(self.table[i])
                    for j in range(len(self.table[i])):
                        if self.table[i][j][1].find(keyword):
                            book_list_key.append(self.table[i][j][0])
        return book_list_key
    def printing_books(self):
        if self.collision_type=="Chain":
            for i in range(self.table_size):
                if self.table[i] is not None:
                    for j in range(len(self.table[i])):
                        print(self.table[i][j][0], end="")
                        print(":", end=" ")
                        print(self.table[i][j][1].__str__())
        else:
            for i in range(self.table_size):
                if self.table[i] is not None:
                    print(self.table[i][0], end="")
                    print(":", end=" ")
                    print(self.table[i][1].__str__())
    
    def get_slot(self, key):
        return super().hash_fun_1(key, self.params[0])%self.table_size
        pass
    
    def get_load(self):
        return self.size/self.table_size
        pass
    
    def __str__(self):
        string=""
        if self.collision_type=="Chain":
            for i in range(self.table_size):
                if self.table[i] is None:
                    string+="<EMPTY> "
                else:
                    for j in range(len(self.table[i])):
                        string+="("
                        string+=self.table[i][j][0]
                        string+=","
                        string+=self.table[i][j][1].__str__()
                        string+=")"
                        if j is not len(self.table[i])-1:
                            string+=";"
                if i is not self.table_size-1:
                    string+="|"
        else:
            for i in range(self.table_size):
                if self.table[i]==None:
                    string+="<EMPTY>"
                else:
                    string+="("
                    string+=self.table[i][0]
                    string+=","
                    string+=self.table[i][1].__str__()
                    string+=")"
                if i is not self.table_size-1:
                    string+="|"
        return string
        pass
