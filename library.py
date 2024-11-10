import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        self.n_books=len(book_titles)
        self.final_list=[]
        for i in range(self.n_books):
            t=self.merge_sort(texts[i])
            texts_list=[]
            j=0
            while(j<len(texts[i])):
                if len(texts_list)>0:
                    if t[j]==texts_list[-1]:
                        j+=1
                    else:
                        texts_list.append(t[j])
                        j+=1
                else:
                    texts_list.append(t[j])
                    j+=1
            self.final_list.append((book_titles[i], texts_list))
        self.final_list=self.merge_sort_2(self.final_list)
        pass
    
    def distinct_words(self, book_title):
        #list of distinct words in that book in lexico
        low=0
        high=len(self.final_list)-1
        the_book=self.binary_search_b(book_title, self.final_list, low, high)
        # print(the_book)
        return the_book[1]
        pass
    
    def count_distinct_words(self, book_title):
        #number of distinct words in that book
        low=0
        high=len(self.final_list)-1
        the_book=self.binary_search_b(book_title, self.final_list, low, high)
        return len(the_book[1])
        pass
    
    def search_keyword(self, keyword):
        #list of books with given keyword
        book_list=[]
        for i in range(len(self.final_list)):
            low=0
            high=len(self.final_list[i][1])-1
            # print("a")
            # print(self.final_list[i][1])
            a = self.binary_search_c(keyword, self.final_list[i][1], low, high)
            # print(a)
            if a!=-1:
                book_list.append(self.final_list[i][0])
        # print(book_list)
        return book_list
        pass
    
    def print_books(self):
        #print title followed by distinct words for all books
        for i in range(len(self.final_list)):
            # print(self.final_list[i][0], end=": ")
            # print(":", end=" ")
            
            # for j in range(len(self.final_list[i][1])):
                # print(self.final_list[i][1][j], end=" ")
                # if j!=(len(self.final_list[i][1])-1):
                #     print("|", end=" ")
            format=" | ".join(self.final_list[i][1])
            print(f"{self.final_list[i][0]}: {format}")

            
            # print()
            
        pass

    def binary_search_b(self, book, final, low, high):
        while low <= high:
            mid = low + (high - low) // 2
            if final[mid][0] == book:
                return final[mid]
            elif final[mid][0] < book:
                low = mid + 1
            else:
                high = mid - 1

        return -1
    
    def binary_search_c(self, book, final, low, high):
        while low <= high:
            mid = low + (high - low) // 2
            if final[mid] == book:
                return final[mid]
            elif final[mid] < book:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def merge_sort_2(self, words):
        if len(words)<=1:
            return words
        mid=len(words)//2
        #left part of the list of words
        left=self.merge_sort(words[:mid])
        #right part of the list of words
        right=self.merge_sort(words[mid:])
        #merge the left and right parts
        return self.merge_2(left,right)
    
    def merge_2(self, left, right):
        sort_list=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i][0]<=right[j][0]:
                sort_list.append(left[i])
                i+=1
            else:
                sort_list.append(right[j])
                j+=1
        sort_list.extend(left[i:])
        sort_list.extend(right[j:])
        return sort_list
    
    def merge_sort(self, words):
        if len(words)<=1:
            return words
        mid=len(words)//2
        #left part of the list of words
        left=self.merge_sort(words[:mid])
        #right part of the list of words
        right=self.merge_sort(words[mid:])
        #merge the left and right parts
        return self.merge(left,right)

    def merge(self, left, right):
        sort_list=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            # print(left[i])
            if left[i]<=right[j]:
                sort_list.append(left[i])
                i+=1
            else:
                sort_list.append(right[j])
                j+=1
        sort_list.extend(left[i:])
        sort_list.extend(right[j:])
        return sort_list

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.name=name
        self.params=params
        if name == "Jobs":
            self.collision_type="Chain"
            self.table=ht.HashMap("Chain", params)
            self.table_size=self.params[1]
        elif name == "Gates":
            self.collision_type="Linear"
            self.table=ht.HashMap("Linear", params)
            self.table_size=self.params[1]
        else:
            self.collision_type="Double"
            self.table=ht.HashMap("Double", params)
            self.table_size=self.params[3]
        pass
    
    def add_book(self, book_title, text):
        words_hash_table=ht.HashSet(self.collision_type, self.params)
        for word in text:
            words_hash_table.insert(word)
        self.table.insert((book_title, words_hash_table))
        pass
    
    def distinct_words(self, book_title):
        hash_set=self.table.find(book_title)
        return hash_set.list_of_words()
        pass
    
    def count_distinct_words(self, book_title):
        hash_set=self.table.find(book_title)
        return hash_set.size
        pass
    
    def search_keyword(self, keyword):
        # book_list_key=[]
        # if self.collision_type=="Double":
        #     for i in range(self.params[3]):
        #         if self.table[i] is not None:
        #             if self.table[i][1].find(keyword):
        #                 book_list_key.append(self.table[i][0])
        # else:
        #     for i in range(self.params[1]):
        #         if self.table[i] is not None:
        #             if self.table[i][1].find(keyword):
        #                 book_list_key.append(self.table[i][0])
        # return book_list_key
        return self.table.find_keyword(keyword)
    pass
    
    def print_books(self):
        # if self.collision_type=="Chain":
        #     for i in range(self.table_size):
        #         if self.table[i] is not None:
        #             for j in range(len(self.table[i])):
        #                 print(self.table[i][j][0], end=" ")
        #                 print(":", end=" ")
        #                 print(self.table[i][j][1].__str__())
        # else:
        #     for i in range(self.table_size):
        #         print(self.table[i][0], end=" ")
        #         print(":", end=" ")
        #         print(self.table[i][1].__str__())
        self.table.printing_books()
        pass
