import EEGPSDChart from "../components/EEGPSDChart";
import EEGSpectrogramChart from "../components/EEGSpectrogramChart";
import EEGBrainImage from "../components/EEGBrainImage";
import EEGState from "../components/EEGState";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Home.css";

const Home = () => {
    const [result, setResult] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const stored = localStorage.getItem("eegResult");
        if (!stored) {
        navigate("/");
        } else {
        setResult(JSON.parse(stored));
        }
    }, []);

    if (!result) return <p>Loading Results...</p>;

    return (
    <div className="home-container">
        <div className="sidebar">
            <EEGBrainImage />
            <EEGState estado={result.estado} color={result.color} />
        </div>
        <div className="scrollable-content">
            <EEGPSDChart psdPath={result.psd_image} />
            <EEGSpectrogramChart spectrogramPath={result.spectrogram_image} />
        </div>
    </div>
    );
};

export default Home;
