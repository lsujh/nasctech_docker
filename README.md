# nasctech_docker
Download container - 
        docker pull lsujh/nasctech:latest

Container run - 
        docker run -p 5000:5000 -d nasctech

request 
        http://0.0.0.0:5000/start/?={'data' : [1, 2, 3, 4, 5], 'rule' : ['a','b','c','d','e','f']}

Way to pass a sequence of rules
{"data" : [1, 2, 3, 4, 5], "rule" : {"a":fun_a, "b":fun_b, "c":fun_b, "d":fun_c, "e":fun_e, "f":fun_f}}
