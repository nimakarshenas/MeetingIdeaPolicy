#!/usr/bin/env python3
import argparse, json
from src.preprocessing.tiering import light_screen, decide_promotion
from src.nlp.pipeline import run_full_nlp

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--utterances", required=True, help="Path to JSON list of utterances")
    args = ap.parse_args()
    utts = json.load(open(args.utterances))
    out = []
    for u in utts:
        scores = light_screen(u.get("text",""))
        decision = decide_promotion(scores)
        if decision.promote:
            u["tier"] = "A"
            u.update(run_full_nlp(u))
        else:
            u["tier"] = "P"
        out.append({**u, "promotion_reason": decision.reason, "scores": decision.scores})
    print(json.dumps(out, indent=2))
