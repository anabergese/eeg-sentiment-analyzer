from domain.state_detector import detect_user_state
from infrastructure.signal_processing import compute_psd


def detect_state(data, eeg_channels, fs):
    return detect_user_state(
        data, eeg_channels, freqs=None, psd_method=compute_psd, fs=fs
    )
