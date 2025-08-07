from brainflow.data_filter import DataFilter


def detect_user_state(data, eeg_channels, freqs, psd_method, fs, threshold=1.0):
    total_beta = 0
    total_theta = 0

    for ch in eeg_channels:
        signal = data[ch, :].astype(float)
        psd, freqs = psd_method(signal, fs)

        psd_tuple = (psd, freqs)
        beta = DataFilter.get_band_power(psd_tuple, 13.0, 30.0)
        theta = DataFilter.get_band_power(psd_tuple, 4.0, 8.0)

        total_beta += beta
        total_theta += theta

    avg_beta = total_beta / len(eeg_channels)
    avg_theta = total_theta / len(eeg_channels)

    print(f"Beta Average: {avg_beta:.4f}")
    print(f"Theta Average: {avg_theta:.4f}")

    if avg_beta > avg_theta * threshold:
        return "Alert", "#D92534"
    elif avg_theta > avg_beta * threshold:
        return "Relaxed", "#32BAD9"
    else:
        return "Indeterminate", "#D7D9D9"
