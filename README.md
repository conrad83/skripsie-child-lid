# Language Identification of South African Child Speech

Code for the final-year project (Project (E) 448, Stellenbosch University) *Language Identification of South African Child Speech* by Conrad Joubert.

The project asks three questions:

1. Can a large pretrained language identification (LID) model identify the language of South African child speech without any adaptation?
2. If not, can a lightweight classifier trained on its frozen embeddings do so, without fine-tuning the model?
3. Does the resulting accuracy reflect the language being spoken, or the recording setup of each corpus?

The languages are Afrikaans, isiXhosa and Sesotho sa Leboa, together with British English and Dutch. The pretrained models are MMS-LID, WavLM and Whisper.

## Repository layout

```
config.py          paths, model IDs and shared settings
01–09_*.ipynb      experiments, in the order of the report
requirements.txt   Python packages
```

| Notebook | What it does | Report |
|---|---|---|
| `01_mms_baseline` | MMS-LID on child speech, no adaptation | Chapter 4, baseline (Table 4.1) |
| `02_adult_baseline` | MMS-LID on adult speech (NCHLT, VoxPopuli) | Chapter 4, baseline (Table 4.1, last column) |
| `03_layer_sweep_mms` | Classifier on every MMS layer, chosen on validation | Chapter 4, layer selection and model comparison |
| `04_layer_sweep_wavlm` | Same for WavLM | Chapter 4 |
| `05_layer_sweep_whisper` | Same for the Whisper encoder | Chapter 4 |
| `06_training_volume` | Accuracy against the number of training speakers | Chapter 4, training volume |
| `07_same_setup_controls` | Binary classifiers on two languages from the same corpus | Chapter 5, same-setup control |
| `08_cross_corpus_controls` | Babaloon Afrikaans test set replaced by SADiLaR Afrikaans | Chapter 5, cross-corpus evaluation |
| `09_british_english_snr` | UMAP, low-level descriptors and SNR equalisation | Chapter 6 |

## Method in short

- Each clip is passed through a frozen pretrained model and every hidden layer is mean-pooled over time (MMS: 1 280 dimensions, WavLM: 768, Whisper encoder: 512, averaged over the real frames only).
- A `StandardScaler` and `LogisticRegression` (`max_iter=1000`, `random_state=42`) are trained on one layer at a time.
- Every language is subsampled to 10 085 utterances and split 80/10/10 into speaker-disjoint train, validation and test sets with `GroupShuffleSplit` (`random_state=42`). British English has no speaker labels and is grouped by recording session.
- The layer is chosen on the validation set, and the test set is used once for the chosen layer.

## Data

No audio or derived data is included. The corpora have to be obtained from their owners:

| Language | Corpus | Access |
|---|---|---|
| Afrikaans, isiXhosa | Babaloon oral narratives (Jacobs et al., 2025; Louw et al., 2025) | On request from the authors |
| Sesotho sa Leboa, Afrikaans | SADiLaR child speech database (Bornman et al., 2023) | https://hdl.handle.net/20.500.12185/690 |
| British English | Nexdata British English child speech | Commercial, https://www.nexdata.ai/datasets/speechrecog/1252 |
| Dutch | CHOREC (Cleuren et al., 2008) | On request from the corpus owners |
| Adult Afrikaans, English, isiXhosa, Sesotho sa Leboa | NCHLT speech corpus (Barnard et al., 2014) | SADiLaR |
| Adult Dutch | VoxPopuli (`facebook/voxpopuli`, `nl`, test split) | Streamed from the Hugging Face hub |

AI (Claude) was used to split these large datasets into utterances using their transcriptions. 

## Running the code

1. Install Python 3.9 and the packages: `pip install -r requirements.txt`. The models are downloaded from the Hugging Face hub on first use.
2. Point `DATA_DIR` in `config.py` (or the `SKRIPSIE_DATA` environment variable) at the folder that holds the prepared clips and manifests.
3. Run the notebooks in order. Notebooks 03–05 extract the embeddings of every layer and take several hours each on a CPU. Notebooks 06–09 load the saved layer-9 MMS embeddings from `EMBEDDINGS/`.

The noise added in notebook 09 is random, so a full rerun of the SNR experiment gives slightly different numbers from the report.
