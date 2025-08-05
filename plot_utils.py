import matplotlib.pyplot as plt


def plot_psd(freqs, psd):
    plt.plot(freqs, psd)
    plt.title("PSD (Welch) - Synthetic Board")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Densidad espectral (uV²/Hz)")
    plt.xlim(0, 45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
