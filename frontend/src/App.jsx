// src/App.jsx
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./App.css";

function App() {
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleAnalyze = async () => {
    setLoading(true);
    try {
      const response = await fetch("/analyze");
      const result = await response.json();
      localStorage.setItem("eegResult", JSON.stringify(result));
      navigate("/home");
    } catch (error) {
      console.error("Error al analizar EEG:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>EEG Visualizer</h1>
      <p>Analiza datos de EEG sintéticos y visualiza las señales y tu estado emocional.</p>
      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? "Analizando..." : "Comenzar Análisis"}
      </button>
    </div>
  );
}

export default App;
