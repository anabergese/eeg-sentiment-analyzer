const EEGSpectrogramChart = ({ spectrogramPath }) => {
    return (
        <div>
            <h2>Spectrogram</h2>
            <img
                src={spectrogramPath}
                alt="Spectrogram Chart"
                style={{ width: "100%" }}
            />
        </div>
    );
};

export default EEGSpectrogramChart;
