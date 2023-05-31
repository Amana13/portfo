from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    # home page
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    # using this, it can handle any html filename for each page
    return render_template(page_name)

def write_to_file(data):
    # writes to a text file for us to respond
    with open('database.txt', newline='', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')
        # returns as a dictionary

def write_to_csv(data):
    # writes to a csv file
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # delimiter seperates each 
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html') #render_template('login.html', error=error)
        except:
            return 'did not save to database'
            # catches any errors that may happen
    else:
        return 'something went wrong'

if __name__ == "__main__":
    app.run(debug=True)
# if FLASK_ENV = "development" not enabling debugger use above code
# and run file from the command line 
