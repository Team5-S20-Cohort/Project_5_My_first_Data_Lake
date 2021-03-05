from flask import Flask, render_template, request, url_for, redirect, flash


app = Flask(__name__) 
app.secret_key = 'ugihvwbiwyriyesklnl831980-1298bhjlkjlkhgjfiyu8903y8u890-98765467788990-9'

streams_list = []
my_routes = {
 
     "MD": ["Covid Analytics"]
  
}


# views 
views = [
        # (view_name, report_id)
("Covid Analytics", "88977c77-5f8d-4e9d-ba25-a1deabdc52df")
]

@app.route("/")                   
def home():                      
    return render_template("index.html")


@app.route("/dashboard")
def render_view():
    # check if user has access to view
   
    # render the first view
    _, report_id = views[0]

    return render_template("report.html", my_routes=my_routes["MD"], 
        reportId=report_id, active_view=None)

@app.route("/about")                   
def about():                      
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)