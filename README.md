# ECG-Based Sudden Cardiac Death Prediction

Research notebooks for ECG-based sudden cardiac death (SCD) early-warning experiments. The repository contains the original exploratory implementation for data construction, baseline modelling, and the ODE-GCN variant. It is provided for research and code reference.

## Included notebooks

| Notebook | Purpose |
| --- | --- |
| `notebooks/7class.ipynb` | Constructs seven pre-event stages from the 35 minutes before an SCD event, splits ECG recordings into 2-second segments, and prepares NSR controls. |
| `notebooks/baseline.ipynb` | Baseline data pipeline and MLP / multi-view ECG MLP experiments. |
| `notebooks/ODE.ipynb` | ODE-GCN experiments with temporal TCN, time-frequency CNN, wavelet transformer, multi-view fusion, graph convolution, and Neural ODE components. |
| `notebooks/early warning.ipynb` | End-to-end early-warning workflow, including ECG preprocessing, time-frequency features, residual TCN embeddings, Top-K graph construction, GCN/Neural ODE, multi-band fusion, and minute-level evaluation. |

Notebook outputs have been cleared before release. The `1.ipynb` plotting notebook and the export manifest are intentionally retained only in the local archive and are not part of the public source release.

## Environment

The notebooks were developed with Python 3.9+ and PyTorch. Install the baseline dependencies with:

```bash
pip install -r requirements.txt
```

Depending on the installed PyTorch version and CUDA environment, you may need to install an appropriate CUDA-enabled PyTorch wheel separately. The workflows use `torchdiffeq`, `wfdb`, NumPy, SciPy, scikit-learn, Matplotlib, Seaborn, PyWavelets, and Jupyter.

## Data and paths

No raw ECG recordings, processed arrays, trained checkpoints, logs, or result figures are included in this repository. Do not distribute participant-level data without confirming its license, ethics approval, and any institutional requirements.

The exported notebooks contain machine-specific absolute paths from the original research environment. Before executing a notebook, replace the SCD and NSR data paths with directories available on your machine. A typical local layout is:

```text
data/
  SCD/
  NSR/
```

Review the dataset documentation and use only a legally authorized source. If data are acquired from PhysioNet or another controlled-access provider, follow that provider's attribution and redistribution terms.

## Evaluation protocol

Use subject-level or Holter-record-level train/validation/test splits. Do not randomly split adjacent 2-second segments from the same recording across different partitions, because this causes leakage and can substantially overestimate performance. Freeze the event definition, pre-event time window, class assignment, random seed, and evaluation metric before comparing models.

## Reproducibility status

This release is an exploratory notebook package, not yet a fully packaged training framework. Preprocessing, training, evaluation, and visualization are interleaved in the notebooks and rely on cell execution order. For a production-quality reproduction, first validate data loading and tensor shapes, then convert the chosen final workflow into `preprocess.py`, `models/`, `train.py`, `evaluate.py`, and versioned configuration files.

## License and citation

No license is included in this initial code release. Obtain the maintainer's permission before redistributing, incorporating the code into a derivative project, or using it commercially. Add the associated manuscript citation here once it is publicly available.
