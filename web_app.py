from flask import Flask, render_template
from flask import request

from chart_retriver import SpotifyTopChart

app = Flask(__name__)

spotify = SpotifyTopChart()

@app.route('/hello')
def hello_world():
   return 'Hello World'


@app.route('/')
def main():
    return render_template('%s.html' % 'musicland')

@app.route('/top_50_chart')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    country = request.args.get('country')
    chart = spotify.get_top_50_chart(country)
    return render_template('%s.html' % 'musicland', top_50_chart=chart)



if __name__ == '__main__':
   app.run()