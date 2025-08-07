const EEGState = ({ estado, color }) => {
    return (
        <div style={{ marginTop: "2rem" }}>
            <h2>Estado emocional detectado</h2>
            <div style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
                <div
                style={{
                    width: "40px",
                    height: "40px",
                    backgroundColor: color,
                    borderRadius: "50%",
                    border: "1px solid #ccc"
                }}
                />
                <span style={{ fontSize: "1.5rem" }}>{estado}</span>
            </div>
        </div>
    );
};

export default EEGState;
