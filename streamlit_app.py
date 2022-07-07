import os
os.system('pip install jupyterlab && npm i -g localtunnel')
os.system('pip install jupyterlab && npm i -g localtunnel')
os.system('jupyter-lab --generate-config')
os.system('echo "c.NotebookApp.allow_remote_access = True" >> /root/.jupyter/jupyter_lab_config.py')
os.system('jupyter-lab --allow-root --no-browser --port 11000 & lt --port 11000')
