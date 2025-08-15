const EEGSpectrogramChart = ({ spectrogramPath }) => {
    return (
        <div>
            <h2>Spectrogram by EEG channel</h2>
            <img
                src={spectrogramPath}
                alt="Spectrogram Chart"
                style={{ width: "100%" }}
            />
        </div>
    );
};

export default EEGSpectrogramChart;
