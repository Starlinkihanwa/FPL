from fpl import FPL

def get_fpl_points(team_id, gameweek=None):
    try:
        fpl = FPL()
        user_team = fpl.get_user(team_id)
        user_team_name = user_team['player_first_name']
        user_team_points = user_team['summary_event_points']

        if gameweek is not None:
            user_team_history = fpl.get_user_history(team_id)
            for gw in user_team_history:
                if gw['event'] == gameweek:
                    return f"{user_team_name}'s points in gameweek {gameweek}: {gw['points']}"
            return f"No data found for gameweek {gameweek}"

        return f"{user_team_name}'s latest FPL points: {user_team_points}"
    except Exception as e:
        return str(e)

def main():
    print("Welcome to the FPL Points Checker!")

    try:
        team_id = int(input("Enter your FPL team ID: "))
        result = get_fpl_points(team_id)

        print(result)

        choice = input("Do you want to check points for a specific gameweek? (yes/no): ").strip().lower()
        if choice == 'yes':
            gameweek = int(input("Enter the gameweek you want to check: "))
            gameweek_result = get_fpl_points(team_id, gameweek)
            print(gameweek_result)
    except ValueError:
        print("Please enter a valid team ID.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


