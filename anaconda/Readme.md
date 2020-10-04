- Backup Environment to Anaconda Cloud and Using it to Setup/Restore Environment
```bash
# Export Environment to yml file 
conda env export -n my-environment -f my-environment.yml

# Upload Env file to Anaconda Cloud 
anaconda upload my-environment.yml

# Setting up Env using Env from Anaconda Cloud
conda env create user/my-environment
source activate my-environment
```

- Upgrade python packages/libraries and launch Jupyter server
```bash
# Upgrade All Packages
conda upgrade --all -y

# Start Jupyter Server
nohup jupyter-lab --port=8888 --ip=0.0.0.0 --no-browser &
```
