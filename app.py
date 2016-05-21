from flask import Flask, render_template, request, jsonify, Markup
import json
import os
import sqlite3 #Database management library we used
import jinja2


#for row in c.execute('SELECT * FROM USIODB'):
#    print row


废物wuxixiang
app = Flask(__name__, static_folder='.', static_url_path='')

# Handler
@app.route("/home.html")
def index():
    return render_template('home.html')
    
@app.route("/pivot_table.html")
def pivot_table():

    # Process the Database
    conn = sqlite3.connect('USIODB.db')
    c = conn.cursor()

    table = html_table(c)
    
#    for sublist in c.execute('SELECT * FROM USIODB'):
#        print sublist
    c.close()
    conn.close()    
    
    return render_template('pivot_table.html',table = Markup(table))

def html_table(c):
    # Generates table
    table = '<table class="table table-striped table-hover">'
    
    header = 1

    for row in c.execute('SELECT * FROM USIODB'):
        
        table += '<tr>'
        if header:
            table+='<thead>'
            for data in row:
                table+='<th>{}</th>'.format(data)
            table+='</thead></tr>'
            header = 0

        else:
        
            for data in row:
                table+='<td>{}</td>'.format(data)
            table+='</tr>'

    table+='</table>'
    return table    

@app.route("/pivot_table_builder.html")
def pivot_table_builder():
    return render_template('pivot_table_builder.html')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8765)
    



