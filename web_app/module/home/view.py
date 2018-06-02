from flask import render_template, Blueprint
module_home = Blueprint(
    'module_home', #name of module
    __name__,
    template_folder='templates' # templates folder
)
@module_home.route('/')
def index():
    return render_template('home.html')