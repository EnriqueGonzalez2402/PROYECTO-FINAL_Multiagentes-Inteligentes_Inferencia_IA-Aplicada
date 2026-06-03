from fastapi import FastAPI

app = FastAPI(
title="AURA Expert System",
description="Sistema experto multiagente para diagnóstico inteligente",
version="1.0"
)

@app.get("/")
def root():
return {
"status": "online",
"system": "AURA"
}
