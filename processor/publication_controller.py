import datetime

from flask import Flask, render_template, request, redirect, url_for

from publicationservice.publication_database_scrapper import publication_updates, update_read_count

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
    update_count, pubs, published_this_year, total_read_from_last_year = publication_updates(now.year)
    # update_count = 1
    # pubs = [PublicationDetails(
    #     "hero__title",
    #     "hero__content",
    #     "content__body",
    #     "bar__title",
    #     "www.google.com",
    #     '2021'
    # )]

    return render_template('publications.html', updates=update_count, publications=pubs,
                           pp=published_this_year, tr=total_read_from_last_year)


@app.route('/publications/', methods=['post'])
def update_read_record():
    if request.method == 'POST':
        read_count = request.form.get('read_count')  # access the data inside
        print(read_count)
        update_read_count(int(read_count))

    return redirect(url_for('publications'))


#TODO
# submit read count
# cache the results
# cache reset
if __name__ == "__main__":
    app.run()
