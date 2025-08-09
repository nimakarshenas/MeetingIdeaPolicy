"""Audio->ASR->Transcript ingestion stub."""
from loguru import logger

def ingest_meeting(meeting_meta: dict, audio_ptr: str) -> dict:
    logger.info("Ingesting meeting %s", meeting_meta.get("meeting_id"))
    # TODO: ASR call, write transcript pointer
    return {"meeting_id": meeting_meta.get("meeting_id"), "transcript_ptr": "s3://.../transcript.json"}
