#Name my gyms and their attributes I want ppl to pick
#low/high budget
#close/far from home
#do you have low motivation/high motivation

gyms = {
    "Peasant Fitness": {"budget": "low", "location": "near", "motivation": "low"},
    "Globo Gym": {"budget": "high", "location": "far", "motivation": "high"},
    "Shark Swim Club": {"budget": "low", "location": "near", "motivation": "low"},
    "Caffeine Running Club": {"budget": "high", "location": "far", "motivation": "high"},
}

def get_gym_recommendation():
    # ask user about budget low/high
    budget = input("Do you have a high or low budget? (low/high):").strip().lower()
    # ask user about location near/far
    location = input("Do you prefer the gym to be near or far? (near/far):").strip().lower()
    # ask user about motivation low/high
    motivation = input("Is your motivation low or high? (low/high):").strip().lower()

# gym suggested based on answers ^^^
    if budget == "low" and location == "near" and motivation == "low":
        print("'Peasant Fitness' is the place for you!") 
    elif budget == "high" and location == "far" and motivation == "high":
        print("'Globo Gym' is the place for you, you Stallion!")
    elif budget == "low" and location == "near" and motivation == "low":
        print("'Shark Swim Club' is for you...get treading or die!")
    elif budget == "high" and location == "far" and motivation == "high":
        print("Joining 'Caffeine Running Club' is better latte than never!")
    else:
        print("You're too cool for a gym! Just go outside!")

#This is the main function that starts the game
def main():
    print("Welcome to your Perfect Gym Finder!")
    
    while True:
        get_gym_recommendation() #this calls the function I made above that handles the logic (if else)

    #ask after they're done if they want to run it again
    repeat = input("Would you like to find another gym? (yes/no):").strip().lower()

    if repeat != "yes":
            print("Thanks for using your Perfect Gym Finder! Goodbye! ")
            break

if __name__ == "__main__":
    main()
