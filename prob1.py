dialy_steps = list(map(int, input("Enter space-separated integers: ").split()))
#input()  takes the entire line of input as a string.
#.split() splits the string into a list of substrings based on spaces.
#map(int, ...) converts each substring into an integer.
#list()   converts the map object into a list.
print(max(dialy_steps))
print(min(dialy_steps))
average = sum(dialy_steps) / len(dialy_steps)
print(average)
print(sorted(dialy_steps, reverse=True))