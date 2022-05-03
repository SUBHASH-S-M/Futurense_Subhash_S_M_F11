import flask
from tkinter_fb_oper import *
from flask import request, jsonify
app=flask.Flask(__name__)
app.config["DEBUG"]=True
books=[
    {
        'id':0,
        'title':'A Fire Upon the Deep',
        'author':'vernor vingo',
        'first_sentense':'The coldsleep itself was dreamless.',
        'year_published':'1992',
    },
    {
        'id':1,
        'title':'The Ones Who Walk Away from omelas',
        'author':'Ursula k.Le Guin',
        'first_sentense':'with a clamor of bells that set the swallows soaring,the festival of summer came to the city omlas,brigh',
        'published':'1975'
    },
    {
        'id':2,
        'title':'Dhalgren',
        'author':'Samuel R. Delany',
        'first_sentense':'to wound the autumnal city',
        'published':'1975'
    }
]
@app.route('/',methods=['GET'])

# def home():
#     app = tkinterApp()
#     app.mainloop()
#     return 'Tkinter open'

@app.route('/books/all',methods=['POST'])
def api_all():
    return jsonify(books)
app.run()