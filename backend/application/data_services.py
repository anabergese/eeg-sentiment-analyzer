from infrastructure.board_interface import get_data_from_board


def read_brain_data(duration_sec=60):
    return get_data_from_board(duration_sec)
