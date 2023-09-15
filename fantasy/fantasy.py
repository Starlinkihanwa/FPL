from flask import Flask, request, jsonify
from fpl import FPL

app = Flask(__name__)

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

@app.route('/api/fpl/points', methods=['GET'])
def api_fpl_points():
    try:
        team_id = int(request.args.get('team_id'))
        result = get_fpl_points(team_id)

        return jsonify({"message": result})
    except ValueError:
        return jsonify({"error": "Please provide a valid team ID."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

