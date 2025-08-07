// src/pages/Home.jsx
import EEGCharts from "../components/EEGCharts";
import EEGState from "../components/EEGState";
import EEGBrainImage from "../components/EEGBrainImage";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
    const [result, setResult] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const stored = localStorage.getItem("eegResult");
        if (!stored) {
        // Si el usuario accede directamente sin pasar por /analyze
        navigate("/");
        } else {
        setResult(JSON.parse(stored));
        }
    }, []);

    if (!result) return <p>Cargando resultados...</p>;

    return (
        <div style={{ display: "flex", gap: "2rem", padding: "2rem" }}>
            {/* Columna izquierda */}
            <div style={{ flex: 1 }}>
                <EEGCharts psdPath={result.psd_image} spectrogramPath={result.spectrogram_image} />
            </div>

            {/* Columna derecha */}
            <div style={{ flex: 1 }}>
                <EEGBrainImage />
                <EEGState estado={result.estado} color={result.color} />
            </div>
        </div>
    );
};

export default Home;
