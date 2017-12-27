with open("rosalind_fibd.txt") as f:
    input_data = f.read().split()
    #print(input_data)
    input_data = list(map(int, input_data))
    #print(input_data)
    total_months = input_data[0]
    life_time = input_data[1]
    #print(total_months)
    #print(life_time)

    #initial_state = []
    #initial_state[0]= 1
    initial_state = [0]*(life_time)
    initial_state[0] = 1
   # initial_state[1] = 1
    #print(initial_state)
    for i in range(total_months-1):
        s = sum(initial_state[1:])
        initial_state.pop()
        initial_state.insert(0,s)
       # print(initial_state)
    answer = sum(initial_state[:])
    print(answer)