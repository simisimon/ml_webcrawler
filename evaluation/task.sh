PROJECTNAME=scikit_learn

LOCALPATH=/tmp/$USER/$PROJECTNAME/$1

# ----------------------------------------------------------------------------
# Prepare file system
# ----------------------------------------------------------------------------
# We create the folder structure the node where the job runs to save some
# network bandwidth.

# Clean up leftovers from previous failed runs
rm -rf $LOCALPATH/

# Create results folder
mkdir -p $LOCALPATH


# ----------------------------------------------------------------------------
# Prepare environment
# ----------------------------------------------------------------------------

# Create and source virtual environment
python3 -m venv $LOCALPATH/venv
source $LOCALPATH/venv/bin/activate


# Install dependencies
wheel="$(find $2 -type f -iname "*.whl")"

pip install $wheel
pip install pandas
pip install gitpython joblib

# Get evaluation script
cp $2/evaluation.py $LOCALPATH
cp $2/scikit_learn_repos.csv $LOCALPATH

# ----------------------------------------------------------------------------
# Run experiment
# ----------------------------------------------------------------------------

python3 evaluation.py $1

# ----------------------------------------------------------------------------
# Copy results
# ----------------------------------------------------------------------------


cp -r $LOCALPATH/out/* $2/results/

# ----------------------------------------------------------------------------
# Clean up
# ------------

deactivate

rm -rf "$LOCALPATH"
