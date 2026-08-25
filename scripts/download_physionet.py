"""Download the PhysioNet databases used by the ECG experiments.

The script downloads data through wfdb's PhysioNet client. It does not
include or redistribute patient-level recordings in this repository.
"""

from __future__ import annotations

import argparse
from pathlib import Path


DATABASES = {
    "scd": "sddb",
    "nsr": "nsrdb",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data"),
        help="Directory in which SCD and NSR subdirectories are created.",
    )
    parser.add_argument(
        "--datasets",
        nargs="+",
        choices=sorted(DATABASES),
        default=sorted(DATABASES),
        help="Datasets to download; defaults to both datasets.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        import wfdb
    except ImportError as exc:
        raise SystemExit(
            "wfdb is required for downloading PhysioNet data. "
            "Install the repository dependencies with: pip install -r requirements.txt"
        ) from exc

    args.output_dir.mkdir(parents=True, exist_ok=True)

    for name in args.datasets:
        target = args.output_dir / name.upper()
        target.mkdir(parents=True, exist_ok=True)
        database = DATABASES[name]
        print(f"Downloading PhysioNet database {database} to {target}")
        wfdb.dl_database(database, dl_dir=str(target))
        print(f"Finished {name.upper()}")


if __name__ == "__main__":
    main()
