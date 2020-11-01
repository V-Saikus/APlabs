from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/api/v1/hello-world-23')
def var():
    return 'Hello World 23'

if __name__=='__main__':
    app.run()