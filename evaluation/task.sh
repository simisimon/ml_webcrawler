wheel="$(find $1 -type f -iname "*.whl")"

pip install $wheel

pip install gitpython joblib


python3 $1/evaluation.py

rm "$wheel"
