// src/App.jsx
import { useState } from "react";
import "./App.css";
import { NUM_REELS, STATIC_SYMBOLS } from "./config/slotConfig";

function App() {
  const [balance, setBalance] = useState(100);

  const handleSpin = () => {
    setBalance((prev) => prev - 1);
  };

  return (
    <div className="app-root">
      <div className="slot-card">
        <h1 className="slot-title">Slot Machine</h1>

        <div className="slot-reels">
          {Array.from({ length: NUM_REELS }).map((_, index) => (
            <div key={index} className="reel">
              <span className="symbol">{STATIC_SYMBOLS[index]}</span>
            </div>
          ))}
        </div>

        <p className="slot-balance">Balance: ${balance}</p>
        <button className="spin-button" onClick={handleSpin}>
          Spin
        </button>
      </div>
    </div>
  );
}

export default App;

