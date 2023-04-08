from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        pass
        # ip = request.form.get('ip')#Gets the note from the HTML 
            # flash('Error joining Mesh Network', category='error') 
    # return render_template("connect.html")