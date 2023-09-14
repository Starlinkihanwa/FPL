import sys
from fpl import FPL

def get_fpl_points(team_id):
    try:
        fpl = FPL()
        user_team = fpl.get_user(team_id)
        user_team_name = user_team['player_first_name']
        user_team_points = user_team['summary_event_points']

        return f"{user_team_name}'s latest FPL points: {user_team_points}"
    except Exception as e:
        return str(e)

def main():
    print("Welcome to the FPL Points Checker!")

    try:
        team_id = int(input("Enter your FPL team ID: "))
        result = get_fpl_points(team_id)
        print(result)
    except ValueError:
        print("Please enter a valid team ID.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

