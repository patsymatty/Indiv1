#!/usr/bin/env python
# coding: utf-8

# In[10]:


from_member = "@joeilagan"
to_member = "@eeebeee"
social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
   "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

def relationship_status(from_member, to_member, social_graph):
    
    if from_member in social_graph and to_member in social_graph:
        From_member = social_graph[from_member]
        To_member = social_graph[to_member]

        if from_member in To_member["following"] and to_member in From_member["following"]:
            return "friends"
        elif from_member in To_member["following"]:
            return "followed by"
        elif to_member in From_member["following"]:
            return "follower"
    else:
        return "no relationship"

relationship_status = relationship_status(from_member, to_member, social_graph)
print(relationship_status)


# In[96]:


board = [
['X','O','O',''],
['O','X','','O'],
['X','','X',''],
['O','X','','O']
]



def tic_tac_toe(board):
    size = len(board)

#checking rows
    for row in range(size):
        if board[row].count('X') == 3:
            return "X"
        elif board[row].count('O') == 3:
            return "O"

#checking columns
    for column in range(size):
        for row in range(size-2): 
            if board[row][column] == board[row+1][column] == board[row+2][column] != '':
                return board[row][column]

#checking diagonals
    for row in range(size-2):
        for (column) in range(size-2):
            if board[row][column] == board[row+1][column+1] == board[row+2][column+2] != '':
                return board[row][column]
        

    return "NO WINNER"


result = tic_tac_toe(board)
print(result)


# In[75]:


first_stop = "admu"
second_stop = "dlsu"
route_map = {

     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

def eta(first_stop, second_stop, route_map):
      
    if (first_stop,second_stop) in route_map.keys():
        travel_time = route_map[(first_stop, second_stop)]["travel_time_mins"]
        return travel_time

result = eta(first_stop, second_stop, route_map)
print(result)    

