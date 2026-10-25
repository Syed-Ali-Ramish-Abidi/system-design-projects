from fastapi import FastAPI, HTTPException

app = FastAPI()

notes = {}
next_id = 1

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/notes")
def create_note(text: str):
    global next_id
    note_id = next_id
    notes[note_id] = text
    next_id += 1
    return {"id": note_id, "text": text}

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"id": note_id, "text": notes[note_id]}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes[note_id]
    return {"message": "Note deleted"}
