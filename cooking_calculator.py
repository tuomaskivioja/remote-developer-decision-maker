

turkey_cooking_time = 14

ham_cooking_time = 5

def cooking_end_time(start_time, duration):
    return (start_time + duration) % 24
   

print(f"take the turkey out of the oven at {cooking_end_time(20, turkey_cooking_time)} o'clock")

print(f"take the ham out of the oven at {cooking_end_time(13, ham_cooking_time)} o'clock")