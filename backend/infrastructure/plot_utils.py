import matplotlib

matplotlib.use("Agg")  # Use a non-interactive backend for plotting
import matplotlib.pyplot as plt
from brainflow.data_filter import DataFilter, WindowOperations
from scipy.signal import spectrogram


def plot_psd(freqs, psd):
    plt.plot(freqs, psd)
    plt.title("PSD (Welch) - Synthetic Board")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Densidad espectral (uV²/Hz)")
    plt.xlim(0, 45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_all_psds(data, eeg_channels, fs, eeg_labels=None):
    n_channels = len(eeg_channels)
    n_cols = 4  # número de columnas en el grid de gráficos
    n_rows = (n_channels + n_cols - 1) // n_cols

    fig, axs = plt.subplots(n_rows, n_cols, figsize=(15, 8))
    axs = axs.flatten()

    for i, ch in enumerate(eeg_channels):
        signal = data[ch, :].astype(float)

        # Calcular PSD usando Welch
        psd, freqs = DataFilter.get_psd_welch(
            signal, 256, 128, fs, WindowOperations.HANNING.value
        )

        label = eeg_labels[i] if eeg_labels else f"Channel {ch}"
        axs[i].plot(freqs, psd)
        axs[i].set_title(label)
        axs[i].set_xlim(0, 45)
        axs[i].set_xlabel("Frecuencia (Hz)")
        axs[i].set_ylabel("PSD")
        axs[i].grid(True)

    # Ocultar subplots vacíos
    for j in range(i + 1, len(axs)):
        axs[j].axis("off")

    fig.suptitle("PSD por canal EEG (Synthetic Board)", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig


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


def show_state_color(state, color):
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.set_facecolor("green" if color == "🟢" else "red")
    ax.text(
        0.5,
        0.5,
        f"{state.upper()}",
        fontsize=20,
        ha="center",
        va="center",
        color="white",
    )
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title("Estado mental detectado")
    plt.show()
