const EEGState = ({ estado, color }) => {
    return (
        <div style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            textAlign: "center",
        }}>
            <h2>
                Emotional State Detected: <span style={{ fontSize: "1.5rem" }}>{estado}</span>
            </h2>
            <div style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
                <div
                style={{
                    width: "300px",
                    height: "300px",
                    backgroundColor: color,
                    border: "1px solid #ccc"
                }}
                />
            </div>
        </div>
    );
};

export default EEGState;
