import os
import sys
from pathlib import Path
from distutils.dir_util import copy_tree


c = get_config()

# Template config
c.JupyterHub.logo_file = 'theme/images/gpnb.png'
c.JupyterHub.template_paths = ['./theme/templates']

# DEV: Copy static assets to the data_files_path directory (wish there were a better way to hand that)
static_path = os.path.join(Path(sys.executable).parent.parent, 'share', 'jupyterhub', 'static')
copy_tree('./theme/css/', os.path.join(static_path, 'css'), update=1)
copy_tree('./theme/images/', os.path.join(static_path, 'images'), update=1)
copy_tree('./theme/js/', os.path.join(static_path, 'js'), update=1)
