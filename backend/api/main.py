import warnings

warnings.filterwarnings("ignore", message="pkg_resources is deprecated.*")

from application.analysis import run_eeg_analysis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/analyze")
def analyze():
    """
    Executes EEG analysis and returns:
    - state: 'alert' or 'relaxed'
    - color: HEX code
    - images: paths to the PSD and spectrogram plots
    """
    result = run_eeg_analysis()
    return result
