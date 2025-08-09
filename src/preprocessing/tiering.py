from dataclasses import dataclass

@dataclass
class PromotionDecision:
    promote: bool
    reason: str
    scores: dict

def light_screen(text: str) -> dict:
    # TODO: implement: lite area router, fast NER count, small emb sim
    return {"area_conf": 0.12, "salient_entities": 0, "sim_to_topic": 0.10}

def decide_promotion(scores: dict) -> PromotionDecision:
    if scores.get("area_conf", 0) >= 0.40:
        return PromotionDecision(True, "area_conf>=0.40", scores)
    if scores.get("salient_entities", 0) >= 1:
        return PromotionDecision(True, "salient_entity>=1", scores)
    if scores.get("sim_to_topic", 0) >= 0.55:
        return PromotionDecision(True, "sim_to_topic>=0.55", scores)
    return PromotionDecision(False, "no_rule_met", scores)
