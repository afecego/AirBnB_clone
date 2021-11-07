# AirBnB_clone

***

## DESCRIPTION

This project is the first step towards building your first full web application: the AirBnB clone. The objective was to create a console that can create a new object, retrieve an object from a file, a database etc., do operations on objects (count, compute stats, etc.), update attributes of an object and destroy an object.

### Learning Objectives

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

***

## HOW TO STAR IT

To star and use the console just type:

~~~
$ ./console
~~~

## HOW TO USE IT

The console works by recognizing the typed command and executes the task defined in the program. Example:

To create a new instance of class "BaseModel":

~~~
(hbnb) create BaseModel
~~~

and the output is:

~~~
49faff9a-6318-451f-87b6-910505c55907
~~~

The list of created commands and their function:

* EOF = To exit the program
* all = Prints all string representation of one or all instances
* create = Creates a new instance of a class
* destroy = Deletes an instance based on the class name and id
* help = List available commands with "help" or detailed help with "help cmd"
* quit = To exit the program
* show = Prints the string representation of an instance
* update = Updates an instance based on the class name and id

If the command receives incorrect information, the output will be error messages. Example:

To create a new instance of class "Otro":

~~~
(hbnb) create Otro
~~~

and the output is:

~~~
** class doesn't exist **
~~~

For a guide to the use of the console, the help command shows the information of the created commands and also informs about the function of each command.

Help for the information of all commands:

~~~
(hbnb) help
~~~

and the output is:

~~~
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
~~~

or help for single command information

~~~
(hbnb) help quit
~~~

and the output is:

~~~
Quit command to exit the program
~~~
