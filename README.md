# Tifinagh decipher

This script is designed to help you find hidden words within a grid image. It uses Optical Character Recognition (OCR) to read the grid from `assets/grid.png` and compares it against a list of words specified in `assets/words.txt`.

## Prerequisites

## Setup

The script comes with a `Makefile` that simplifies the setup process. The following command will install all necessary packages listed in `requirements.txt`.

```bash
make setup-python
```

## Usage

To use the script, you need to have a grid image saved as `assets/grid.png` and a text file with the words to search for as `assets/words.txt` - each word should be on a new line.

You can use the follwowing command to activate the python virtual environment:

```bash
make shell
```

Once you have the assets in place, you can initiate the search with the following command:

```bash
make search
```

## Related resources

The idea comes from a [LinkedIn challenge](https://www.linkedin.com/posts/billatnapier_alice-has-hidden-20-secret-words-related-activity-7158901180838920192-SUZ1) so as the default image in `assets/`. If you want to generate your own grid you can do it [here](https://asecuritysite.com/ctf/ctf_grid).