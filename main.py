import asyncio
import json
import math
import random
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse

app = FastAPI(title="Trânsito Inteligente Indaiatuba - API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SensorDataProcessor:
    def __init__(self, max_distance_cm=1000):
        self.max_distance_cm = max_distance_cm
        self.last_readings = {}

    def filter_ultrasonic_noise(self, current_dist, node_id, threshold_jump=300):
        if node_id in self.last_readings:
            prev_dist = self.last_readings[node_id]['dist_cm']
            if abs(current_dist - prev_dist) > threshold_jump and current_dist > self.max_distance_cm:
                return prev_dist
        return min(current_dist, self.max_distance_cm)

    def process_telemetry(self, raw_payload):
        node_id = raw_payload.get("node_id")
        timestamp = raw_payload.get("timestamp", time.time())
        speed_kmh = float(raw_payload.get("speed_kmh", 0))
        dist_cm = self.filter_ultrasonic_noise(float(raw_payload.get("dist_cm", 1000)), node_id)

        now = timestamp
        prev = self.last_readings.get(node_id)
        
        deceleration_ms2 = 0.0
        is_hard_braking = False

        if prev:
            dt = now - prev['time']
            if dt > 0:
                v_prev_ms = prev['speed_kmh'] / 3.6
                v_curr_ms = speed_kmh / 3.6
                if v_prev_ms > v_curr_ms:
                    deceleration_ms2 = round((v_prev_ms - v_curr_ms) / dt, 2)
                    if deceleration_ms2 >= 3.0:
                        is_hard_braking = True

        dist_norm = max(0.0, min(1.0, dist_cm / self.max_distance_cm))
        decel_norm = max(0.0, min(1.0, deceleration_ms2 / 8.0))
        risk_score = int(round((0.6 * decel_norm + 0.4 * (1.0 - dist_norm)) * 100))

        processed_event = {
            "node_id": node_id,
            "timestamp": now,
            "speed_kmh": speed_kmh,
            "dist_cm": dist_cm,
            "deceleration_ms2": deceleration_ms2,
            "risk_score": risk_score,
            "hard_braking": is_hard_braking
        }

        self.last_readings[node_id] = {
            "time": now,
            "speed_kmh": speed_kmh,
            "dist_cm": dist_cm
        }

        return processed_event

processor = SensorDataProcessor()
freadas_acumuladas = 23

async def telemetry_event_generator():
    global freadas_acumuladas
    ruas = [
        "Av. Presidente Kennedy",
        "Rua Humaitá",
        "Av. Eng. Fábio Roberto Barnabé",
        "Rua Barão de Itaici"
    ]
    
    while True:
        horario_atual = time.strftime("%H:%M:%S")
        vel_med = round(random.uniform(39.0, 44.5), 1)
        fluxo = random.randint(52, 65)
        risco = random.randint(60, 78)

        evento = None
        if random.random() > 0.55:
            freadas_acumuladas += 1
            v_antes = random.randint(48, 62)
            v_depois = random.randint(12, 28)
            decel = round((v_antes - v_depois) / 3.6 / random.uniform(1.2, 2.2), 1)
            dist = random.randint(280, 750)
            risco_evt = int(round((0.6 * (decel / 8.0) + 0.4 * (1.0 - dist / 1000.0)) * 100))
            
            evento = {
                "horario": horario_atual,
                "rua": random.choice(ruas),
                "vel_antes": v_antes,
                "vel_depois": v_depois,
                "decel": decel,
                "dist": dist,
                "risco": min(99, max(20, risco_evt))
            }

        payload = {
            "velocidade_media": vel_med,
            "fluxo_veiculos": fluxo,
            "freadas_hoje": freadas_acumuladas,
            "risco_global": risco,
            "ponto_grafico": {
                "hora": horario_atual,
                "fluxo": fluxo,
                "vel": vel_med
            },
            "evento_frenagem": evento
        }

        yield f"data: {json.dumps(payload)}\n\n"
        await asyncio.sleep(2.5)

@app.get("/")
async def get_dashboard():
    return FileResponse("dashboard.html")

@app.get("/api/v1/stream")
async def stream_live_data():
    return StreamingResponse(telemetry_event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)