# nasctech_docker

Python file functions.py contains 6 functions.

Your task is to create a back-end service with one end-point (f.e. /start) with the following properties:

1. It can receive a REST GET request with the following structure (f.e):

{'data' : [1, 2, 3, 4, 5], 'rule' : ['a','b','c','d','e','f']}

where 'data' - a list of numbers (float, int) of undefined length, 'rule' - a list (sequence) of rules to be executed upon the 'data' list.

2. Your service should take a sentence of 'rules', match it with functions from the functions.py, and append functions to the 'data' list in the same order.

3. The order of rules may vary, repeat, but contain only provided 6 functions.

4. The response should be as following (f.e.):

{'result' : [5.1, 5.4, 5.9, 6.6, 7.5]}

5. Your solution should be scalable for any number of functions in functions.py (in theory).

6. The resulting server should be put in a docker container.

7. Extra task: Propose your own way to pass a sequence of rules instead of a 'rule' list.

## Cloning & Run:

Download container - 
        docker pull lsujh/nasctech:latest

Container run - 
        docker run -p 5000:5000 -d nasctech

request 
        http://0.0.0.0:5000/start/?={'data' : [1, 2, 3, 4, 5], 'rule' : ['a','b','c','d','e','f']}

Way to pass a sequence of rules
{"data" : [1, 2, 3, 4, 5], "rule" : {"a":fun_a, "b":fun_b, "c":fun_b, "d":fun_c, "e":fun_e, "f":fun_f}}
