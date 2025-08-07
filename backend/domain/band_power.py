from brainflow.data_filter import DataFilter


def get_band_powers(psd, freqs):
    def band_power(psd_tuple, f1, f2):
        return DataFilter.get_band_power(psd_tuple, f1, f2)

    psd_tuple = (psd, freqs)
    bands = {
        "delta (1–4 Hz)": band_power(psd_tuple, 1.0, 4.0),
        "theta (4–8 Hz)": band_power(psd_tuple, 4.0, 8.0),
        "alpha (8–13 Hz)": band_power(psd_tuple, 8.0, 13.0),
        "beta (13–30 Hz)": band_power(psd_tuple, 13.0, 30.0),
    }
    return bands
