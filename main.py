import warnings

warnings.filterwarnings("ignore", message="pkg_resources is deprecated.*")

from band_power import get_band_powers
from board_interface import get_data_from_board
from plot_utils import show_state_color
from signal_processing import compute_psd, preprocess_signal
from state_detector import detect_user_state


def main():
    data, fs, eeg_channels = get_data_from_board()
    signal = data[eeg_channels[0], :].astype(float)

    filtered_signal = preprocess_signal(signal, fs)
    psd, freqs = compute_psd(filtered_signal, fs)

    bands = get_band_powers(psd, freqs)
    for name, value in bands.items():
        print(f"{name}: {value:.4f}")

    # Detectar estado emocional
    estado, color = detect_user_state(
        data, eeg_channels, freqs=None, psd_method=compute_psd, fs=fs
    )
    print(f"Estado detectado: {estado} {color}")
    show_state_color(estado, color)


if __name__ == "__main__":
    main()
