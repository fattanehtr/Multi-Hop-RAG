import subprocess

def run_tests():
    subprocess.run(["python", "-m", "unittest", "discover", "tests"])

def run_api():
    subprocess.run(["python", "modules/api/api_endpoints.py"])

def evaluate_model():
    subprocess.run(["python", "evaluation/evaluate.py"])

if __name__ == "__main__":
    run_tests()
    run_api()
    evaluate_model()