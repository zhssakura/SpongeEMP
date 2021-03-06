from flask import Flask, g
from .autodoc import auto
from .sponge_emp import Sponge_Flask_Obj
from .Site_Main_Flask import Site_Main_Flask_Obj
from .database import DBData

from .utils import debug, SetDebugLevel


app = Flask(__name__)
app.register_blueprint(Sponge_Flask_Obj)
app.register_blueprint(Site_Main_Flask_Obj)
# init the autodoc module
auto.init_app(app)

SetDebugLevel(2)

# init the global database structure
debug(6, 'loading database...')
# dbdata = DBData(biomfile='data/final.withtax.biom', mapfile='data/map.txt', filepath=app.root_path)
dbdata = DBData(biomfile='data/spongeemp.sub5k.biom', mapfile='data/map.txt', filepath=app.root_path)
dbdata.import_data()
debug(6, 'starting server')


# whenever a new request arrives, connect to the database and store in g.db
@app.before_request
def before_request():
    global dbdata

    g.db = dbdata


# and when the request is over, disconnect
@app.teardown_request
def teardown_request(exception):
    pass


if __name__ == '__main__':
    print('pita')
    app.run(debug=True)
