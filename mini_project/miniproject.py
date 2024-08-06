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


#This is the main function that starts the game
def main():
    print("Welcome to your Perfect Gym Finder!")
    get_gym_recommendation()

if __name__ == "__main__":
    main()
