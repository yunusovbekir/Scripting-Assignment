# Scripting Assignment

A Small app to get MAC address information from https://macaddress.io.

## Installation - on Docker

```bash
# clone repo to your machine
git clone git@github.com:yunusovbekir/Scripting-Assignment.git

# create an 'env' file and add the API key to the 'env' file
echo API_KEY=<your API key> > .env
```

## Installation - on locale machine

```bash
# add API key to env variables
export API_KEY="<your API key>"

# create a virtual environment
python -m venv .venv

# activate the virtual environment
source .venv/bin/activate

# install the dependencies
pip install -r requirements.txt
```

## Usage

```bash
# run with docker
docker-compose run --rm app python app.py <MAC address you are looking for>

# run on locale machine
python app.py <MAC address you are looking for>
```