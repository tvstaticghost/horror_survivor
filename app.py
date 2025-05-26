from flask import Flask, render_template
from data import info

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', horror_season=info.horror_survivor_season, starting_tribes=info.starting_tribes, predictions=info.predictions, shelter_events=info.shelter_events, starting_alliances=info.starting_alliances,
                           immunity_challenges=info.immunity_challenges, immunity_challenge_winners=info.immunity_challenge_winners)

if __name__ == '__main__':
    app.run(debug=True)