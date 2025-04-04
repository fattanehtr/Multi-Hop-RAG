import json
from sklearn.metrics import f1_score

def evaluate(predictions, gold_answers):
   
    f1_scores = []
    for pred, gold in zip(predictions, gold_answers):
        f1_scores.append(f1_score(gold, pred, average='micro'))
    return sum(f1_scores) / len(f1_scores)

if __name__ == "__main__":
   
    with open("data/hotpotqa.json", "r") as f:
        data = json.load(f)

    predictions = []
    gold_answers = []
    
    f1 = evaluate(predictions, gold_answers)
    print(f"F1 Score: {f1}")