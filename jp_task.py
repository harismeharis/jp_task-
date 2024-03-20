def calculate_active_durations(events):
    
    active_times = {}
    stack = []
    last_time = None

    for event in events:
        name, action, time = event

        if action == "start":
            # If there's an active event, then update its active time,
            # up to the current event's start
            if stack:
                active_event = stack[-1]
                if active_event in active_times:
                    active_times[active_event] = active_times[active_event] + time - last_time
                else:
                    active_times[active_event] = time - last_time
            stack.append(name)
            last_time = time
            
        elif action == "end":
            if stack:
                active_event = stack.pop()
                if active_event in active_times:
                    active_times[active_event] = active_times[active_event] + time - last_time
                else:
                    active_times[active_event] = time - last_time
                last_time = time

    return ', '.join([f"{name} {duration}" for name, duration in active_times.items()])


# Examples

events1 = [
    ('a', 'start', 0),
    ('b', 'start', 1),
    ('c', 'start', 2),
    ('c', 'end', 3),
    ('b', 'end', 4),
    ('a', 'end', 5)
]

events2 = [
    ('x', 'start', 1),
    ('y', 'start', 2),
    ('z', 'start', 3),
    ('z', 'end', 4),
    ('y', 'end', 5),
    ('x', 'end', 6)
]

events3 = [
    ('m', 'start', 0),
    ('n', 'start', 1),
    ('o', 'start', 2),
    ('p', 'start', 3),
    ('p', 'end', 6),
    ('o', 'end', 8),
    ('n', 'end', 9),
    ('m', 'end', 14)
]

events4 = [
    ('f', 'start', 0),
    ('g', 'start', 2),
    ('g', 'end', 4),
    ('f', 'end', 7)
]


events5 = [
    ('x', 'start', 2),
    ('y', 'start', 4),
    ('z', 'start', 7),
    ('z', 'end', 11),
    ('y', 'end', 12),
    ('x', 'end', 14),
    ('x', 'start', 17),
   ('x', 'end', 19)
]


events6 = [
    ('x', 'start', 7),
    ('y', 'start', 8),
    ('z', 'start', 17),
    ('z', 'end', 19),
    ('y', 'end', 21),
    ('x', 'end', 29),
    ('x', 'start', 80),
   ('x', 'end', 190)
]


events7 = [
    ('x', 'start', 7),
    ('y', 'start', 8),
    ('z', 'start', 17),
    ('z', 'end', 19),
    ('y', 'end', 21),
    ('x', 'end', 29),
    ('k', 'start', 80),
   ('k', 'end', 190)
]



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




# Calculate and print the active durations for each example
print(calculate_active_durations(events1))
print(calculate_active_durations(events2))
print(calculate_active_durations(events3))
print(calculate_active_durations(events4))
print(calculate_active_durations(events5))
print(calculate_active_durations(events6))
print(calculate_active_durations(events7))
print(calculate_active_durations(events8))

