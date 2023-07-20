#!/usr/bin/env python
# coding: utf-8

# In[19]:


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


# In[80]:


board = [
    ['X', 'O', 'X', ''],
    ['', 'X', 'X', ''],
    ['X', '', 'X', 'O'],
    ['X', '', 'X', 'X']
]
def tic_tac_toe(board):
    size = len(board)

# checking rows and columns
    for i in range(size):
        row_result = check_line(board, i, 0, 0, 1, size)
        col_result = check_line(board, 0, i, 1, 0, size)
        if row_result or col_result:
            return row_result or col_result

# checking diagonals and reverse diagonals
    for i in range(size - 2):
        diagonal_result = check_line(board, i, i, 1, 1, size)
        reverse_diagonal_result = check_line(board, i, size - i - 1, 1, -1, size)
        if diagonal_result or reverse_diagonal_result:
            return diagonal_result or reverse_diagonal_result

    return "NO WINNER"

def check_line(board, row, col, dx, dy, size):
    start = board[row][col]
    if start == '':
        return None

    for i in range(1, size):
        if row + dx*i >= size or col + dy*i >= size or board[row + dx*i][col + dy*i] != start:
            return None

    return start

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

