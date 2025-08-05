import warnings

warnings.filterwarnings("ignore", message="pkg_resources is deprecated.*")

from band_power import get_band_powers
from board_interface import get_data_from_board
from plot_utils import plot_psd
from signal_processing import compute_psd, preprocess_signal


def main():
    data, fs, eeg_channels = get_data_from_board()
    signal = data[eeg_channels[0], :].astype(float)

    filtered_signal = preprocess_signal(signal, fs)
    psd, freqs = compute_psd(filtered_signal, fs)

    bands = get_band_powers(psd, freqs)
    for name, value in bands.items():
        print(f"{name}: {value:.4f}")

    plot_psd(freqs, psd)


if __name__ == "__main__":
    main()
