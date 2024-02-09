# KI Videoprojekt Reinforcement Learning

## Installation

install

- [python](https://www.python.org/downloads/)
- a latex distribution ([texlive](https://www.tug.org/texlive/))
- [ffmpeg](https://ffmpeg.org/download.html)
- [pre-commit](https://pre-commit.com/) (development only)

```bash
pip install -r requirements.txt

# For Development also run

pre-commit install
```

## Usage

```bash
# low quality
python -m ai101_video 
# or
python -m ai101_video --quality high_quality
```

You can see all available options with `python -m ai101_video --help`. Note that the multiprocessing option does not work as exprected and suld only be used for testing purposes.

If audio is missing sometimes, try to run the script with the `--disable_caching` flag.

## Jupyter Notebook

There exists a [Jupyter Notebook](./reinforcement_learning.ipynb) for the scenario "Frozen Lake" used in the video.

## Video-Script

The script for the video can be found [here](./KI_Video_Script.pdf).
