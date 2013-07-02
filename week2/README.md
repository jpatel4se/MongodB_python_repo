##Introduction to week 2
Nothing significant to note down
##CRUD and Mongo Shell
Create = Insert
Read = Find
Update = Update
Delete = remove
##Secrets of Mongo Shell

###Mongo shell is interactive javascript interpreter.
for (i=0; i<3; i++) print("hello");
hello
hello
hello

###Help Mongodb

help

### Javascript variable declaration

> z={A:1} 
{ "A" : 1 }
> z.a
> z.A
1

> z["A"]
1
> w="A"
A
> z["w"]
> w
A
> z[w]
1
### Quiz 
What does the following fragment of JavaScript output? 
x = { "a" : 1 };
y = "a";
x[y]++;
print(x.a);

2

##BSON Introduced

###1. We can map Javascript object to Json dictionary.

###2 Javascript object is suitable for use as mongodb document.

 obj = {"a": 1, "b": 3, "c":["appless", "bananas"]}
{ "a" : 1, "b" : 3, "c" : [ "appless", "bananas" ] }

###3. Mongodb uses Binary json representation named BSON for storing data inside documents

#### Bson provides more datatypes on top of JSON.
for e.g.
	|	"\x05" e_name binary	Binary data
			
	|	"\x07" e_name (byte*12)	ObjectId

			
			
	|	"\x09" e_name int64	UTC datetime
	|	"\x10" e_name int32	32-bit Integer
	|	"\x11" e_name int64	Timestamp

#### Quiz 
Which of the following are types available in BSON?
 Strings Floating-point numbers Complex numbers Arrays Objects Timestamps
###Mongo shell, inserting docs

####Inserting javascript object
 obj = {"a": 1, "b": 3, "c":["appless", "bananas"]}
{ "a" : 1, "b" : 3, "c" : [ "appless", "bananas" ] }
db.week2.insert(obj)
db.week2.find()
{ "_id" : ObjectId("51d236bdb085920b572961ba"), "a" : 1, "b" : 3, "c" : [  "appless",  "bananas" ] }

####Quiz 
Insert a document into the "fruit" collection with the attributes of "name" being "apple", "color" being "red", and "shape" being round. Assume that we have already issued the use command to get into the right database. Use the "insert" method.
<pre><code>

db.fruit.insert({"name":"apple", "color":"red", "shape":"round"})
</pre></code>

### Mongoshell - introduction to findone

####findone() retrieves random document from collection. It might help us determine schema of collection.





