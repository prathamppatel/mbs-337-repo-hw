from dash import Dash, html

"""
A minimal Dash web application that displays 'Hello, World!'.
"""

app = Dash()
server = app.server

app.layout = [html.Div(children='Hello, World!')]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)