loss = 1
iteration=0
max_iteration=50
while loss > 0.01 and iteration < max_iteration:

    loss*=0.9
    iteration+=1
    
    print(f"iteration {iteration}, loss {loss}")
