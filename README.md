# jp_task-


The code follows the stack approach with the help of a dictionary, which we discussed during the exercise.
I have included test cases, along with some ‘exotic’ ones which test more tricky behaviours like test case ‘events8’ where events start after 0 tilmestep, events open and close multiple times (z) and events are starting after a ‘dead’ period (nothing happening) like z in the example bellow.
The algorithm works as I expect based on my understanding of the requirements. If I have not understood something please feel free to let me know.

events8 = [
    ('x', 'start', 7),
    ('y', 'start', 8),
    ('z', 'start', 17),
    ('z', 'end', 19),
    ('y', 'end', 21),
    ('x', 'end', 29),
    ('z', 'start', 80),
   ('z', 'end', 190)
]

My output here is :
x 9, y 11, z 112

Based on my understanding of the requirements this is correct because.

X starts at 7 and stops at 8 ->  so 1 timestep for x
Y starts at 8 and stops at 17 -> so 9  timesteps for y
Z starts at 17 and ends at 19 -> so 2 timesteps for z
After z ends, y kicks of again and ends at 21 -> so 2 extra timesteps for y => 9+2 = 11 in total for y
After y ends, x ends at 29 -> so 8 extra timesteps for x => 1+ 8 =9 in total for x
After x ends there is a dead period until tilmestep 80.
At tilmestep 80 z starts again until tilmestep 190 -> so 110 extra timesteps for z => 110 + 2 = 112 in total for z

The algorithm works as I expect based on my understanding of the requirements. If I have not understood something please feel free to let me know.
The key structs are a list that behaves like a stack memory (stack) and a dictionary (active_times) which calculates the active times on the fly as we parse the input list.
