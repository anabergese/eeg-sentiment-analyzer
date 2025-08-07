import matplotlib

matplotlib.use("Agg")  # Use a non-interactive backend for plotting
import matplotlib.pyplot as plt
from scipy.signal import spectrogram


def plot_all_spectrograms(data, eeg_channels, fs, eeg_labels=None):
    n_channels = len(eeg_channels)
    n_cols = 4  # columnas en la grilla de gráficos
    n_rows = (n_channels + n_cols - 1) // n_cols

    fig, axs = plt.subplots(n_rows, n_cols, figsize=(15, 10))
    axs = axs.flatten()

    for i, ch in enumerate(eeg_channels):
        signal = data[ch, :].astype(float)
        f, t, Sxx = spectrogram(signal, fs=fs, nperseg=256, noverlap=128)

        label = eeg_labels[i] if eeg_labels else f"Channel {ch}"
        pcm = axs[i].pcolormesh(t, f, Sxx, shading="gouraud")
        axs[i].set_title(label)
        axs[i].set_ylim(0, 45)
        axs[i].set_xlabel("Tiempo (s)")
        axs[i].set_ylabel("Frecuencia (Hz)")

    for j in range(i + 1, len(axs)):
        axs[j].axis("off")

    fig.suptitle("Espectrogramas por canal EEG (Synthetic Board)", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.colorbar(pcm, ax=axs.tolist(), label="Potencia", shrink=0.6)
    return fig
