from flask import Flask, render_template

app = Flask(__name__)

#main route:  Return response to prompt user to add 'play' to route in order to render template. 
@app.route('/')
def inital():
    print("playground")
    return "Add '/play' to the browser to enter the playground"

#render template that display three blue boxes
@app.route('/play')
def main():
    print("playground")
    return render_template('index.html', columns=3)

#When a user visits localhost:5000/play/(x), have it display boxes x based on what is pased through the route. 
@app.route('/play/<int:columns>')
def xOfColumns(columns):
    return render_template('index.html', columns=columns)
    
#When a user visits localhost:5000/play/(x), have it display boxes x amount of times and the boxes appear as the color passed through the route. 
@app.route('/play/<int:columns>/<color_change>')
def colorAndColumns(columns, color_change):
    colorChange = color_change
    return render_template('colorindex.html',columns=columns, colorChange=colorChange)

if __name__=="__main__":
    app.run(debug=True)