const EEGCharts = ({ psdPath, spectrogramPath }) => {
    return (
        <div>
            <h2>Power Spectral Density (PSD)</h2>
            <img src={psdPath} alt="PSD Chart" style={{ width: "100%", marginBottom: "2rem" }} />

            <h2>Espectrogramas</h2>
            <img src={spectrogramPath} alt="Spectrogram Chart" style={{ width: "100%" }} />
        </div>
    );
};

export default EEGCharts;
