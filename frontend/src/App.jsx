import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

// src/App.jsx

function App() {
  const [balance, setBalance] = useState(100);

  return (
    <div style={{ 
      minHeight: "100vh", 
      display: "flex", 
      justifyContent: "center", 
      alignItems: "center", 
      background: "#111", 
      color: "#f5f5f5" 
      }}
      >
      <div style={{ 
        padding: "2rem", 
        borderRadius: "1rem", 
        background: "#222", 
        boxShadow: "0 0 20px rgba(0,0,0,0.6)", 
        textAlign: "center" 
        }}
        >
        <h1>Slot Machine</h1>
        <p>Balance: ${balance}</p>
        <button 
        style={{ 
          marginTop: "1rem", 
          padding: "0.5rem 1.5rem", 
          borderRadius: "999px", border: "none", 
          fontSize: "1rem", cursor: "pointer" 
          }}
          onClick={() => setBalance(balance - 1)}
        >
          Spin
        </button>
      </div>
    </div>
  );
}

export default App;
