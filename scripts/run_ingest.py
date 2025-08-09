#!/usr/bin/env python3
import argparse, json
from src.ingestion.ingest import ingest_meeting

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True, help="Path to meeting metadata JSON")
    ap.add_argument("--audio", required=True, help="Pointer/URL to audio")
    args = ap.parse_args()
    meta = json.load(open(args.meta))
    res = ingest_meeting(meta, args.audio)
    print(json.dumps(res, indent=2))
