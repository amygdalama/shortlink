from flask import Flask, render_template, request, redirect
app = Flask(__name__)

def read_cache(filename='cache.txt'):
    cache = {}
    with open(filename) as f:
        for line in f:
            key, value = line.split('\t')
            cache[key] = value.rstrip().lstrip('http://')
    return cache


def link_cache(link):
    cache = read_cache()
    shortened_link = str(len(cache))
    while shortened_link in cache:
        shortened_link = str(len(cache))

    return shortened_link


@app.route('/', methods=['GET', 'POST'])
def index():
    with open('cache.txt', 'a') as f:
        if request.method == 'POST':
            link = request.form['link']
            new_link = link_cache(link)
            f.write(new_link + '\t' + link + '\n')
            render_template('index.html', link=link, new_link=new_link)

    return render_template('index.html', link=None, new_link=None)

@app.route('/<link_index>')
def link_page(link_index):
    cache = read_cache()
    if link_index in cache:
        return redirect('http://' + cache[link_index])
    else:
        return "No!"


if __name__ == '__main__':
    app.run(debug=True)
