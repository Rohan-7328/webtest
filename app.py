
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Definieer het datetimefilter
@app.template_filter('datetimefilter')
def datetimefilter(value, format='%Y-%m-%d %H:%M:%S'):
    """Convert a datetime to a different format."""
    if isinstance(value, datetime):
        return value.strftime(format)
    return value

# Je bestaande route
@app.route('/')
def index():
    player = {
        "personaname": "Nicknets",
        "profileurl": "https://steamcommunity.com/id/nicknets",
        "loccountrycode": "NL",
        "lastlogoff": datetime.now(),
        "avatarfull": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/83/83b11f25d63153b5de49cd25a012215b8a8f4b4e_full.jpg"
    }
    total_games = 55
    recent_games = [
        {"name": "Frostpunk", "playtime_forever": 1921},
        {"name": "DOOM Eternal", "playtime_forever": 2197}
    ]
    return render_template('MaNiJeRo.html', player=player, total_games=total_games, recent_games=recent_games)

if __name__ == '__main__':
    app.run(debug=True)
# app.py
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Route voor de startpagina
@app.route('/')
def index():
    # Dummy data voor testdoeleinden
    player = {
        "personaname": "Nicknets",
        "profileurl": "https://steamcommunity.com/id/nicknets",
        "loccountrycode": "NL",
        "lastlogoff": datetime.now(),
        "avatarfull": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/83/83b11f25d63153b5de49cd25a012215b8a8f4b4e_full.jpg"
    }
    total_games = 55
    recent_games = [
        {"name": "Frostpunk", "playtime_forever": 1921},
        {"name": "DOOM Eternal", "playtime_forever": 2197}
    ]
    return render_template('MaNiJeRo.html', player=player, total_games=total_games, recent_games=recent_games)

if __name__ == '__main__':
    app.run(debug=True)

