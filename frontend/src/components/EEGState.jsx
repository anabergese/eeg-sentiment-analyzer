const EEGState = ({ estado, color }) => {
    return (
        <div>
            <div>
                <div
                style={{
                    width: "100%vw",
                    height: "100px",
                    backgroundColor: color,
                }}
                >
                    <h2 style={{ color: "white" }}>
                        Emotional State Detected: {estado}
                    </h2>
                </div>
            </div>
        </div>
    );
};

export default EEGState;
