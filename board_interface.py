import pprint
import time

from brainflow.board_shim import BoardIds, BoardShim, BrainFlowInputParams


def get_data_from_board(duration_sec=60):
    BoardShim.enable_dev_board_logger()
    params = BrainFlowInputParams()
    board_id = BoardIds.SYNTHETIC_BOARD.value
    board = BoardShim(board_id, params)
    descr = BoardShim.get_board_descr(board_id)
    pprint.pprint(descr)
    try:
        board.prepare_session()
        board.start_stream()
        time.sleep(duration_sec)
        data = board.get_board_data()
        print("Data received from the board:", data.shape)
    finally:
        try:
            board.stop_stream()
        except Exception:
            pass
        try:
            board.release_session()
        except Exception:
            pass

    fs = BoardShim.get_sampling_rate(board_id)
    print(f"Sampling rate: {fs} Hz")
    eeg_channels = BoardShim.get_eeg_channels(board_id)
    print(f"EEG channels: {eeg_channels}")
    return data, fs, eeg_channels
