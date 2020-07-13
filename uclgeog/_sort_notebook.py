from pathlib import Path; 
import json;

infile=Path.home().joinpath('.jupyter','jupyter_notebook_config.json')
try:
  y=json.load(open(infile,'r'))    
  # notebooks in notebooks
  y['NotebookApp']['notebook_dir']="notebooks";
  # switch extensions on
  y['NotebookApp']['nbserver_extensions']['jupyter_nbextensions_configurator']=True
  # dump
  json.dump(y,open(infile,'w')) 
except:
  pass
