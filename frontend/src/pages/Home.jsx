import EEGPSDChart from "../components/EEGPSDChart";
import EEGSpectrogramChart from "../components/EEGSpectrogramChart";
import EEGBrainImage from "../components/EEGBrainImage";
import EEGState from "../components/EEGState";
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

    if (!result) return <p>Loading Results...</p>;

    return (
        <div style={{ display: "flex", gap: "2rem", padding: "2rem" }}>
            <div style={{ flex: 1 }}>
                <EEGPSDChart psdPath={result.psd_image} />
                <EEGSpectrogramChart spectrogramPath={result.spectrogram_image} />
            </div>
            <div style={{ flex: 1 }}>
                <EEGBrainImage />
                <EEGState estado={result.estado} color={result.color} />
            </div>
        </div>
    );
};

export default Home;
