from flask import Flask, render_template
from data import info

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404

@app.route('/')
def home():
    return render_template('index.html', horror_season=info.horror_survivor_season, starting_tribes=info.starting_tribes, predictions=info.predictions, shelter_events=info.shelter_events, starting_alliances=info.starting_alliances,
                           immunity_challenges=info.immunity_challenges, immunity_challenge_winners=info.immunity_challenge_winners, tribal_councils=info.tribal_councils, tribal_vote_outs=info.tribal_vote_outs, random_events=info.random_events,
                           final_votes=info.final_votes, recap_tribes=info.recap_tribes, recap_alliances=info.recap_alliances,
                           merge_tribes=info.merge_tribes, merge_info = info.merge_info, merge_alliances=info.merge_alliances)

if __name__ == '__main__':
    app.run(debug=True)
