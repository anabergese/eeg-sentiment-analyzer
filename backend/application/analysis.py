from application.data_services import read_brain_data
from application.plot_services import export_all_plots
from application.state_services import detect_state
from domain.eeg_labels import get_eeg_labels


def run_eeg_analysis():
    data, fs, eeg_channels = read_brain_data()

    eeg_labels = get_eeg_labels()

    export_all_plots(data, eeg_channels, fs, eeg_labels)

    estado, color_emoji = detect_state(data, eeg_channels, fs)

    return {
        "estado": estado,
        "color": color_emoji,
        "psd_image": "/static/psd.png",
        "spectrogram_image": "/static/spectrogram.png",
    }


# STATIC_DIR = "static"

# def run_eeg_analysis():
#     os.makedirs(STATIC_DIR, exist_ok=True)

#     data, fs, eeg_channels = get_data_from_board(duration_sec=60)

#     eeg_labels = "Fz,C3,Cz,C4,Pz,PO7,Oz,PO8,F5,F7,F3,F1,F2,F4,F6,F8".split(",")

#     # Export plots as PNG
#     fig_psd = plot_all_psds(data, eeg_channels, fs, eeg_labels)
#     fig_psd.savefig(os.path.join(STATIC_DIR, "psd.png"))

#     fig_spec = plot_all_spectrograms(data, eeg_channels, fs, eeg_labels)
#     fig_spec.savefig(os.path.join(STATIC_DIR, "spectrogram.png"))

#     # Detect Mental State
#     estado, color_emoji = detect_user_state(
#         data, eeg_channels, freqs=None, psd_method=compute_psd, fs=fs
#     )

#     return {
#         "estado": estado,
#         "color": color_emoji,
#         "psd_image": "/static/psd.png",
#         "spectrogram_image": "/static/spectrogram.png",
#     }
