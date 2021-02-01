import datetime

from flask import Flask, render_template, request, redirect, url_for

from publicationservice.publication_database_scrapper import publication_updates
from publicationservice.publication_details import PublicationDetails

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/')
def hello():
    return render_template('hello.html', name="name")


@app.route('/loop/')
def loop():
    l = [str(f"These are few {i}") for i in range(11)]
    return render_template('loop.html', rows=l)


@app.route('/publications/')
def publications():
    now = datetime.datetime.now()
    # update_count, record_count, pubs = publication_updates(now.year)
    update_count = 1
    record_count = 1
    pubs = [PublicationDetails(
        "hero__title",
        "hero__content",
        "content__body",
        "bar__title",
        "www.google.com"
    )]

    return render_template('publications.html', updates=update_count, records=record_count, publications=pubs)


@app.route('/publications/', methods=['post'])
def login():
    if request.method == 'POST':
        username = request.form.get('read_count')  # access the data inside
        print("form data")
        print(username)

        if username == 'root':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"

    return redirect(url_for('publications'))


#TODO
# submit read count
# cache the results
# cache reset
if __name__ == "__main__":
    app.run()
