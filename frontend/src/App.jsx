// src/App.jsx
import { useState } from "react";
import "./App.css";

function App() {
  const [balance, setBalance] = useState(100);

  const handleSpin = () => {
    setBalance((prev) => prev - 1);
  };

  return (
    <div className="app-root">
      <div className="slot-card">
        <h1 className="slot-title">Slot Machine</h1>
        <p className="slot-balance">Balance: ${balance}</p>
        <button className="spin-button" onClick={handleSpin}>
          Spin
        </button>
      </div>
    </div>
  );
}

export default App;
