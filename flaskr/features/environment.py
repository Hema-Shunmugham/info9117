import os
import sys

cwd = os.path.abspath(os.path.dirname(__file__))
project = os.path.basename(cwd)
new_path = cwd.strip(project)
full_path = os.path.join(new_path,'flaskr')

try:
    from flaskr import app
except ImportError:
    sys.path.append(full_path)
    from flaskr import app

def before_feature(context, feature):
    context.client = app.test_client()


