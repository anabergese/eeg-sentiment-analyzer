const EEGPSDChart = ({ psdPath }) => {
    return (
        <div>
            <h2>Power Spectral Density (PSD)</h2>
            <img
                src={psdPath}
                alt="PSD Chart"
                style={{ width: "100%", marginBottom: "2rem" }}
            />
        </div>
    );
};

export default EEGPSDChart;
