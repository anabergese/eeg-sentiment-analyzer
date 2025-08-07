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
        navigate("/");
        } else {
        setResult(JSON.parse(stored));
        }
    }, []);

    if (!result) return <p>Loading Results...</p>;

    return (
    <div
        style={{
            display: "flex",
            height: "100vh",
            overflow: "hidden",
        }}
        >
        <div
            style={{
            flex: "0 0 40%",
            position: "sticky",
            top: 0,
            height: "100vh",
            overflow: "hidden",
            padding: "2rem",
            borderRight: "1px solid #ddd",
            }}
        >
            <EEGBrainImage />
        </div>
        <div
            style={{
            flex: 1,
            overflowY: "auto",
            padding: "2rem",
            }}
        >
            <EEGState estado={result.estado} color={result.color} />
            <EEGPSDChart psdPath={result.psd_image} />
            <EEGSpectrogramChart spectrogramPath={result.spectrogram_image} />
        </div>
        </div>
    );
};

export default Home;
