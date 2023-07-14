#!/usr/bin/env python
# coding: utf-8

# In[78]:


from_member = "@bongolpoc"
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
        
    return "no relationship"

relationship_status = relationship_status(from_member, to_member, social_graph)
print(relationship_status)


# In[5]:


board = [
['','O','','O'],
['O','X','O',''],
['X','','','O'],
['O','X','','X']
]



def tic_tac_toe(board):
    size = len(board)

#checking rows
    for row in range(size):
        if board[row].count('X') == 3 and '' not in board[row]:
            return "X"
        elif board[row].count('O') == 3 and '' not in board[row]:
            return "O"


#checking columns
    for column in range(size):
        for row in range(size-2): 
            if board[row][column] == board[row+1][column] == board[row+2][column] != '':
                return board[row][column]

#checking diagonals
    for row in range(size - 2):
        for column in range(size - 2):
            if board[row][column] == board[row + 1][column + 1] == board[row + 2][column + 2] != '':
                return board[row][column]

#checking reverse diagonals
    for row in range(size - 2):
        for column in range(size - 1, size - 3, -1):
            if board[row][column] == board[row + 1][column - 1] == board[row + 2][column - 2] != '':
                return board[row][column]
        

    return "NO WINNER"


result = tic_tac_toe(board)
print(result)


# In[3]:


first_stop = "2"
second_stop = "7"
route_map = {

     ("1","2"):{
         "travel_time_mins":10
     },
     ("2","3"):{
         "travel_time_mins":35
     },
     ("3","4"):{
         "travel_time_mins":55
     },
     ("4","5"):{
        "travel_time_mins": 10
     },
     ('5','6'):{
        'travel_time_mins': 10230
     },
     ('6','7'):{
        'travel_time_mins': 1
     }
}

def eta(first_stop, second_stop, route_map):
    
    if (first_stop, second_stop) in route_map: #check if there is a direct route
        return route_map[(first_stop, second_stop)]["travel_time_mins"]

    passed_stops = [first_stop]
    current_stop = first_stop
    travel_time = 0

    while current_stop != second_stop: #continues until it arrives at second stop
        for stop in route_map:
            if stop[0] == current_stop and stop[1] not in passed_stops:
                travel_time += route_map[stop]["travel_time_mins"] #adds each stop passed by to travel time
                current_stop = stop[1]
                passed_stops.append(current_stop)
                break

    return travel_time

result = eta(first_stop, second_stop, route_map)
print(result)

