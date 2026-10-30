#PATHS AND SETTINGS SHARED BY ALL NOTEBOOKS
#Set SKRIPSIE_DATA to the folder that holds the corpora, or edit DATA_DIR below
import os
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("SKRIPSIE_DATA", "/Users/conarj/Documents/4thYear/Skripsie/CODE_AND_DATA"))

#Saved embeddings and generated audio
NOISY_DIR = DATA_DIR / "NOISY_AUDIO"      #SNR-matched copies of the child speech (09)
RESULTS_DIR = REPO_DIR / "results"

#Child speech: (manifest, audio folder)
CHILD = {
    "afr": (DATA_DIR / "babaloon_afr_new/manifest.csv",   DATA_DIR / "babaloon_afr_new/segments_16k"),     #Babaloon
    "xho": (DATA_DIR / "babaloon_xho_child/manifest.csv", DATA_DIR / "babaloon_xho_child/segments_16k"),   #Babaloon
    "nso": (DATA_DIR / "nso/manifest.csv",                DATA_DIR / "nso/segments_16k"),                  #SADiLaR
    "eng": (DATA_DIR / "british_english/manifest.csv",    DATA_DIR / "british_english/16kHz_Mono"),        #Nexdata, one folder per session
    "nld": (DATA_DIR / "chorec_nld/manifest.csv",         DATA_DIR / "chorec_nld/segments_16k"),           #CHOREC
}
#SADiLaR Afrikaans, only used for the same-setup control (07) and the cross-corpus test (08)
CHILD_AFR_SADILAR = (DATA_DIR / "sadilar_afr_new/manifest.csv", DATA_DIR / "sadilar_afr_new/segments_16k")

#Adult speech for the baseline (02): NCHLT corpus root per language, audio in <root>/audio/<speaker>/
ADULT_NCHLT = {
    "afr": DATA_DIR / "nchlt_afr",
    "eng": DATA_DIR / "nchlt_eng",
    "nso": DATA_DIR / "nchlt_nso",
    "xho": DATA_DIR / "nchlt_xho",
}

(REPO_DIR / "EMBEDDINGS").mkdir(exist_ok=True)



