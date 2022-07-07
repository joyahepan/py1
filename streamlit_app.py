import os
os.system('pip install jupyterlab && npm i -g localtunnel')
os.system('rm /root/.jupyter/jupyter_lab_config.py -Rf')
os.system('jupyter-lab --generate-config)
os.system('echo "c.NotebookApp.allow_remote_access = True" >> /root/.jupyter/jupyter_lab_config.py')
os.system('jupyter-lab --allow-root --no-browser --port 10000 & lt --port 10000')
