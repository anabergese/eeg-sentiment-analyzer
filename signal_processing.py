from brainflow.data_filter import (
    DataFilter,
    DetrendOperations,
    FilterTypes,
    WindowOperations,
)


def preprocess_signal(signal, fs):
    DataFilter.detrend(signal, DetrendOperations.CONSTANT.value)
    DataFilter.perform_bandpass(
        signal, fs, 25.0, 49.0, 4, FilterTypes.BUTTERWORTH.value, 0
    )
    return signal


def compute_psd(signal, fs, nfft=256, overlap=128):
    return DataFilter.get_psd_welch(
        signal, nfft, overlap, fs, WindowOperations.HANNING.value
    )
