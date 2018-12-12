import os

from flask import Flask, render_template, request

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
    127.0.0.1 -> only my local machine
    0.0.0.0 -> push this out t
    app.run(host='0.0.0.0',
            port=int(os.environ.get('PORT', 33507))
            )
