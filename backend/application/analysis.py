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
