"""Small shortener."""
import hashlib
import time

from flask import Flask, redirect, render_template, request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis')


@app.route('/<short_url>')
def short_url(short_url):
    """Redirect url."""
    url = r.get(short_url)
    return redirect(url)

@app.route('/')
def root():
    return redirect(request.url_root + 'short')

@app.route('/short', methods=['GET', 'POST'])
def short_link():
    """Short link."""
    if request.method == 'GET':
        return render_template('short.html')
    elif request.method == 'POST':
        url = str(request.form['url'])
        url_hash = (url + str(time.time())).encode('utf-8')
        url_hash = hashlib.md5(url_hash).hexdigest()
        url_hash = url_hash[:8]
        r.set(url_hash, url)
        return request.url_root + url_hash


if __name__ == '__main__':
    app.run(host='0.0.0.0', processes=8)
