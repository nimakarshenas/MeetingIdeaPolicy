"""Full NLP for Tier‑A: embeddings, NER+linking, sentiment, stance, topic assignment."""
def run_full_nlp(utt: dict) -> dict:
    # TODO: implement actual models
    return {
        "embedding_id": "vec_123",
        "sentiment": 0.1,
        "stance": "neutral",
        "topics": [{"topic_id": "t_abc", "score": 0.72}],
        "entities": [{"entity_id": "e_xyz", "salience": 0.4}],
    }
