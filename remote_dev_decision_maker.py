loneliness_is_dealbreaker = input("Remote development can be lonely - is this a dealbreaker to you? (yes/no)").lower() == "yes"
wlb_is_dealbreaker = input("Remote development can lead to difficulties separating work and life - is this a dealbreaker to you? (yes/no)").lower() == "yes"
distractions_is_dealbreaker = input("Remote development as a digital nomad can make it hard to focus on work due to FOMO - is this a dealbreaker to you? (yes/no)").lower() == "yes"

if loneliness_is_dealbreaker or wlb_is_dealbreaker or distractions_is_dealbreaker:
    print("Don't become a demote dev")
else:
    remote_trial_time = 0
    while remote_trial_time < 6:
        print(f"Considering remote development for {remote_trial_time} months...")
        remote_trial_time += 1
    decision = input("Did I love my experience as a remote dev?")
    if decision == "yes":
        print("Become a remote dev")
    else:
        print("Don't become a demote dev")

    