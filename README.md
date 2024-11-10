# Library-Digitalisation-using-Hashing
Made a compressed dictionary for each book in the library to keep record of the distinct words used. <br/>
Implemented two libraries: <br/>
1) using merge sort to perform functions<br/>
2) using hashing: linear probing, chaining and double hashing to handle collisions<br/>
The expected time complexities of finding the distinct words corresponding to a book, the count of distinct words, printing the book record and searching the books corresponding to a given word of some book reduced after implementing hashing.<br/>
For merge sort library:<br/>
distinct words:O(D + log k)<br/>
count of distinct words:O(log k) <br/>
search keyword:O(k log D)<br/>
print books:O(kD) <br/>
For hashing library:<br/>
distinct words:O(table size)<br/>
count of distinct words:O(1) <br/>
search keyword:O(k)<br/>
print books:O(k table size) <br/>
Also implemted dynamic hashing to resize the table size if the current table size had load factor greater than 0.5. This will not waste any space and will increase the size of the table only when required.

