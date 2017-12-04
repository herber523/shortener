import hashlib
import time

from flask import Flask, redirect, render_template, request
import redis

app = Flask(__name__)
r = redis.Redis()

@app.route('/<short_url>')
def short_url(short_url):
    url = r.get(short_url)
    return redirect(url)

@app.route('/short', methods=['GET', 'POST'])
def query_link_view():
    """Get user input."""
    if request.method == 'GET':
        return render_template('short.html')
    elif request.method == 'POST':
        url = str(request.form['url'])
        url_hash = (url + str(time.time())).encode('utf-8')
        url_hash = hashlib.md5(url_hash).hexdigest()
        url_hash = url_hash[:8]
        r.set(url_hash, url)
        return url_hash


if __name__ == '__main__':
    app.run()
