import datetime
import io

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, send_file

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


@app.route('/images/')
def images():
    return render_template("images.html", title="something", url="http://localhost:5000/images/")

@app.route('/figure/')
def figure():
    fig = draw_polygons()
    img = io.BytesIO()
    fig.savefig(img)
    # img.seek(0)
    return send_file(img, mimetype='image/png')


import base64


@app.route('/plot/')
def plot():
    img = io.BytesIO()
    y = [1, 2, 3, 4, 5]
    x = [0, 2, 1, 3, 4]

    plt.plot(x, y)

    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('plot.html', plot_url=plot_url)


def draw_polygons():
    df = pd.DataFrame({'from': ['A', 'B', 'C', 'B'], 'to': ['D', 'A', 'E', 'C']})
    df

    # Build your graph
    G = nx.from_pandas_edgelist(df, 'from', 'to')

    # Graph with Custom nodes:
    nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=40)
    output = io.BytesIO()
    # FigureCanvas(plt.figure()).print_png(output)

    return plt.figure()


#TODO
# submit read count
# cache the results
# cache reset
if __name__ == "__main__":
    app.run()
