import os

from board_interface import get_data_from_board
from plot_utils import plot_all_psds, plot_all_spectrograms
from signal_processing import compute_psd
from state_detector import detect_user_state

STATIC_DIR = "static"


def run_eeg_analysis():
    os.makedirs(STATIC_DIR, exist_ok=True)

    data, fs, eeg_channels = get_data_from_board(duration_sec=60)

    eeg_labels = "Fz,C3,Cz,C4,Pz,PO7,Oz,PO8,F5,F7,F3,F1,F2,F4,F6,F8".split(",")

    # Export plots as PNG
    fig_psd = plot_all_psds(data, eeg_channels, fs, eeg_labels)
    fig_psd.savefig(os.path.join(STATIC_DIR, "psd.png"))

    fig_spec = plot_all_spectrograms(data, eeg_channels, fs, eeg_labels)
    fig_spec.savefig(os.path.join(STATIC_DIR, "spectrogram.png"))

    # Detect Mental State
    estado, color_emoji = detect_user_state(
        data, eeg_channels, freqs=None, psd_method=compute_psd, fs=fs
    )

    return {
        "estado": estado,
        "color": color_emoji,
        "psd_image": "/static/psd.png",
        "spectrogram_image": "/static/spectrogram.png",
    }
