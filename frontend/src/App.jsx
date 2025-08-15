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
      <img src="https://caputron.com/cdn/shop/files/BraiNet-1020-Electrode-Placement-Cap.jpg" alt="EEG Cap" style={{ width: "300px", height: "300px" }} />
      <h1>EEG Visualizer</h1>
      <p>Explore synthetic EEG data, visualize brain activity, and understand your emotional state.</p>
      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? (
          <>
            Analyzing...
            <img
              src="/spinnerGIF.gif"
              alt="Loading data"
              style={{
                width: "10px",
                height: "10px",
                marginLeft: "10px",
                verticalAlign: "middle",
              }}
            />
          </>
        ) : (
          "Run Analysis"
        )}
      </button>
    </div>
  );
}

export default App;
