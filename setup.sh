# WARNING!: YOU *MUST* SOURCE THIS FILE, NOT RUN IT AS AN EXECUTABLE
# assumes that venv is available
python3 -m venv .
source bin/activate
pip install -r requirements.txt
cat <<EOF
########################################
To source the local dependancies run:

source bin/activate
-----------------
To unsource run:

deactivate
-----------------
**BY DEFAULT THIS SCRIPT RUNS bin/activate FOR YOU**
#######################################
EOF
