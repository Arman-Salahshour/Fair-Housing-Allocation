# INSTK5000/9000 Project 1: Student Housing Allocation

Evaluation of a housing officer and four automatic algorithms (A1 to A4) for accuracy and
fairness, using the 2500 student housing applications in `data.csv`.

## Repository structure

```
.
├── data.csv                             the 2500 applications, features + HO/A1-A4 decisions + target
├── constants.py                         paths, column groups, fairness margin, plotting theme
├── preprocessing.py                     loading and tidying of data.csv (grades cleaning, helper columns)
├── 01_data_analysis.ipynb               section 2 of the assignment
├── 02_performance_metrics.ipynb         section 3
├── 03_predictive_parity.ipynb           section 4.1
├── 04_equality_of_false_negatives.ipynb section 4.2
├── 05_subgroup_fairness.ipynb           section 4.3
├── 06_algorithm_analysis.ipynb          section 5
├── figures/                             figures written by the notebooks
├── results/                             result tables written by the notebooks
└── requirements.txt
```

Section 6 of the assignment, data hazards, will be added.

## Installation

Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
jupyter lab
```

Run the notebooks **in numerical order** and use Restart Kernel and Run All Cells in each one.
Every notebook loads and tidies `data.csv` on its own through `preprocessing.load_house_df()`,
so nothing depends on a kernel left over from another notebook. The order matters only because
later notebooks read the result tables written to `results/` by earlier ones:

| Notebook | reads from `results/` | writes to `results/` |
|---|---|---|
| 01 | - | - |
| 02 | - | `performance_metrics.csv` |
| 03 | - | `predictive_parity_age.csv`, `predictive_parity_international.csv` |
| 04 | `performance_metrics.csv`, both predictive parity tables | `false_negatives_age.csv`, `false_negatives_international.csv` |
| 05 | all four fairness tables | `subgroup_predictive_parity.csv`, `subgroup_false_negatives.csv` |
| 06 | `performance_metrics.csv` | `algorithm_summary.csv` |

`figures/` and `results/` are created automatically on import of `constants.py`.

To run everything from the command line instead:

```bash
for nb in 0*.ipynb; do jupyter nbconvert --to notebook --execute --inplace "$nb"; done
```

## Shared code

`constants.py` holds everything used in more than one notebook: the path to the data, the
output folders, the fairness margin (5 percentage points), the column groups (sensitive,
relevant, continuous, decision columns, and so on) and `set_project_theme()`, which every
notebook calls so all figures share one theme and one set of colours.

`preprocessing.py` holds `load_house_df()`, the tidying performed and explained in
`01_data_analysis.ipynb`: the grade format audit, the conversion of the three grade formats to
a common 0 to 100 scale, mean imputation of the missing grades, and the `international_bin`
and `age_group` helper columns.

## Where the answers are

| Assignment question | Notebook |
|---|---|
| Size and types of features, sensitive and relevant features, recommendations | 01 |
| Relationships between features, correlations, plots | 01 |
| Accuracy, precision, recall, F1 and which metric fits | 02 |
| Predictive parity for `international` and for age | 03 |
| Equality of false negatives for `international` and for age | 04 |
| Both metrics on the four `international` x age subgroups | 05 |
| Which features drive A1 to A4, complexity and interpretability | 06 |
