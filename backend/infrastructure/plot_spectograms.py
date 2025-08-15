import matplotlib

matplotlib.use("Agg")  # Use a non-interactive backend for plotting
import matplotlib.pyplot as plt
from scipy.signal import spectrogram


def plot_all_spectrograms(data, eeg_channels, fs, eeg_labels=None):
    n_channels = len(eeg_channels)
    n_cols = 2  # columnas en la grilla de gráficos
    n_rows = (n_channels + n_cols - 1) // n_cols

    fig, axs = plt.subplots(n_rows, n_cols, figsize=(12, n_rows * 3.5))
    axs = axs.flatten()

    last_pcm = None

    for i, ch in enumerate(eeg_channels):
        signal = data[ch, :].astype(float)
        f, t, Sxx = spectrogram(signal, fs=fs, nperseg=256, noverlap=128)

        label = eeg_labels[i] if eeg_labels else f"Channel {ch}"
        pcm = axs[i].pcolormesh(t, f, Sxx, shading="gouraud")
        last_pcm = pcm

        axs[i].set_title(
            label,
            color="white",
            fontsize=10,
            fontweight="bold",
            pad=10,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#6145d6", edgecolor="none"),
        )
        axs[i].set_ylim(0, 45)
        axs[i].set_xlabel("Tiempo (s)")
        axs[i].set_ylabel("Frecuencia (Hz)")

    for j in range(i + 1, len(axs)):
        axs[j].axis("off")

    # fig.suptitle("Espectrogramas por canal EEG (Synthetic Board)", fontsize=16)
    cbar_ax = fig.add_axes([0.2, 0.03, 0.6, 0.02])  # [left, bottom, width, height]
    fig.colorbar(last_pcm, cax=cbar_ax, orientation="horizontal", label="Potencia")

    plt.tight_layout(rect=[0, 0.06, 1, 0.95])

    return fig
