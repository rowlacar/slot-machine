# backend/main.py

from fastapi import FastAPI, HTTPException
from slot_engine import GameSession
from pydantic import BaseModel
from simulation import run_simulation

app = FastAPI()
session = GameSession(starting_balance=100, bet_per_spin=1)

class BetRequest(BaseModel):
    bet_per_spin: int

class SessionState(BaseModel):
    balance: int
    bet_per_spin: int

class SpinResult(BaseModel):
    grid_reel_major: list[list[str]]
    grid_row_major: list[list[str]]
    multiplier: int
    win: int
    balance: int

class SimulationRequest(BaseModel):
    num_spins: int

@app.post("/bet")
def update_bet(request: BetRequest):
    try:
        session.set_bet(request.bet_per_spin)
        return {
            "balance": session.balance,
            "bet_per_spin": session.bet_per_spin
        }
    except (TypeError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/spin", response_model=SpinResult)
def spin():
    """
    Spin the slot machine using the shared GameSession.
    """
    try:
        result = session.spin()
        return result
    except ValueError as e:
        # e.g. "Insufficient balance for spin."
        raise HTTPException(status_code=400, detail=str(e))

# Session
@app.get("/session", response_model=SessionState)
def get_session_state():
    return {
        "balance": session.balance,
        "bet_per_spin": session.bet_per_spin
    }

# Reset
@app.post("/reset")
def reset_session():
    session.balance = 100
    session.bet_per_spin = 1
    return {
        "message": "Session reset.",
        "balance": session.balance,
        "bet_per_spin": session.bet_per_spin
    }

# Simulate
@app.post("/simulate")
def simulate(req: SimulationRequest):
    result = run_simulation(req.num_spins)
    return result
