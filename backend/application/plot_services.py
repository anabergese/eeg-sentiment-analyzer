import os

from infrastructure.plot_utils import plot_all_psds, plot_all_spectrograms

STATIC_DIR = "static"


def export_all_plots(data, eeg_channels, fs, eeg_labels):
    os.makedirs(STATIC_DIR, exist_ok=True)

    fig_psd = plot_all_psds(data, eeg_channels, fs, eeg_labels)
    fig_psd.savefig(os.path.join(STATIC_DIR, "psd.png"))

    fig_spec = plot_all_spectrograms(data, eeg_channels, fs, eeg_labels)
    fig_spec.savefig(os.path.join(STATIC_DIR, "spectrogram.png"))
