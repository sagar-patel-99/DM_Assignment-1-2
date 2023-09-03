# a) Install dependencies
python -m venv env
source env/bin/activate
pip install -r requirements.txt

# b) Run all necessary parts of the codebase
# Run the main program
python main.py &

# Run the tests
pytest test_calculator.py &
