from flask import Flask, request, render_template_string

app = Flask(__name__)

# Strona główna z formularzem
@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        return render_template_string('''
            <!doctype html>
            <html>
                <head>
                    <title>Powitanie</title>
                </head>
                <body>
                    <h1>Cześć, tu Zoja! Witaj, {{ name }}!</h1>
                    <a href="/">Wróć</a>
                </body>
            </html>
        ''', name=name)
    return '''
        <!doctype html>
        <html>
            <head>
                <title>Powitanie</title>
            </head>
            <body>
                <form method="post" action="/">
                    <label for="name">Wpisz swoje imię:</label>
                    <input type="text" id="name" name="name" required>
                    <button type="submit">OK</button>
                </form>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
