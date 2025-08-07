# Ejercicio: PSD y potencias por banda con la Synthetic Board de BrainFlow
# pip install brainflow numpy matplotlib
import warnings

warnings.filterwarnings("ignore", message="pkg_resources is deprecated.*")

import time

import matplotlib.pyplot as plt
import numpy as np
from brainflow.board_shim import BoardIds, BoardShim, BrainFlowInputParams
from brainflow.data_filter import (
    DataFilter,
    DetrendOperations,
    FilterTypes,
    WindowOperations,
)

# 1) Configuración de BrainFlow y tablero sintético
BoardShim.enable_dev_board_logger()  # logs útiles en consola
params = BrainFlowInputParams()  # sin parámetros = synthetic por defecto
board_id = BoardIds.SYNTHETIC_BOARD.value
board = BoardShim(board_id, params)

try:
    board.prepare_session()
    board.start_stream()  # comienza el streaming en memoria
    time.sleep(10)  # deja que se llenen buffers ~10s
    # 2) Descarga de datos y limpieza
    data = board.get_board_data()  # saca todo lo que haya en el buffer
finally:
    # se ejecuta incluso si hubo excepciones arriba
    try:
        board.stop_stream()
    except Exception:
        pass
    try:
        board.release_session()
    except Exception:
        pass

eeg_chs = BoardShim.get_eeg_channels(board_id)
fs = BoardShim.get_sampling_rate(board_id)

# Tomamos un canal para el ejemplo
sig = data[eeg_chs[0], :].astype(np.float64)

# Detrend + bandpass (1–50 Hz) para quedarnos con EEG típico
DataFilter.detrend(sig, DetrendOperations.CONSTANT.value)
DataFilter.perform_bandpass(
    sig,
    fs,
    15.0,
    30.0,
    4,  # fc=15, ancho=30 (≈0–30) -> ajusta a 1–50 si prefieres:
    FilterTypes.BUTTERWORTH.value,
    0,
)
# Alternativa más explícita:
# DataFilter.perform_bandpass(sig, fs, 25.0, 50.0, 4, FilterTypes.BUTTERWORTH.value, 0)
# DataFilter.perform_bandstop(sig, fs, 50.0, 4.0, 2, FilterTypes.BUTTERWORTH.value, 0)  # notch si hay red

# 3) PSD con Welch
nfft = 256
overlap = nfft // 2
psd, freqs = DataFilter.get_psd_welch(
    sig, nfft, overlap, fs, WindowOperations.HANNING.value
)


# 4) Potencias por banda
def band_power(psd, freqs, f1, f2):
    return DataFilter.get_band_power((psd, freqs), f1, f2)


bands = {
    "delta (1–4 Hz)": band_power(psd, freqs, 1.0, 4.0),
    "theta (4–8 Hz)": band_power(psd, freqs, 4.0, 8.0),
    "alpha (8–13 Hz)": band_power(psd, freqs, 8.0, 13.0),
    "beta (13–30 Hz)": band_power(psd, freqs, 13.0, 30.0),
}


print("Potencia por banda (uV^2/Hz aprox.):")
for name, val in bands.items():
    print(f"  {name}: {val:.4f}")

# 5) Gráfico simple de la PSD
plt.figure()
plt.plot(freqs, psd)
plt.title("PSD (Welch) - Synthetic Board")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("PSD")
plt.xlim(0, 45)
plt.show()
