"""Loading and tidying of data.csv, exactly as done in 01_data_analysis.ipynb."""

import numpy as np
import pandas as pd

from constants import DATA_PATH

__all__ = ['LETTER_ORDER', 'detect_grade_format', 'to_comparable_value',
           'standardize_grades', 'load_house_df']

LETTER_ORDER = {'F': 1, 'D': 2, 'C': 3, 'B': 4, 'A': 5}


def detect_grade_format(grades):
    """Label each grade by the recording format it was written in.
    Only what is visible in the value itself is used, never the student's group,
    so the cleaning step cannot leak the sensitive feature into the result."""
    numeric = pd.to_numeric(grades, errors='coerce')

    return pd.Series(
        np.select(
            [grades.isna(), numeric.isna(), numeric <= 10],
            ['missing', 'letter', 'numeric_0_10'],
            default='numeric_0_100'
        ),
        index=grades.index,
    )


def to_comparable_value(value):
    """Turn a grade into a number that is ordered correctly inside its own format."""
    if pd.isna(value):
        return np.nan

    value = str(value).strip().upper()

    if value in LETTER_ORDER:
        return float(LETTER_ORDER[value])

    return float(value)


def standardize_grades(grades):
    """Standardize grades as the student's percentile inside their own recording format.
    The formats do not share a scale and cannot be converted into each other, so a student
    is compared only with the students recorded the same way. Returns the percentile on a
    0 to 100 scale together with the detected format."""
    grade_format = detect_grade_format(grades)
    comparable = grades.apply(to_comparable_value)
    percentile = pd.Series(np.nan, index=grades.index)

    for fmt in grade_format.unique():
        if fmt == 'missing':
            continue
        mask = grade_format == fmt
        percentile[mask] = comparable[mask].rank(pct=True) * 100

    return percentile, grade_format


def load_house_df(path=DATA_PATH):
    """Read data.csv and apply the tidying steps of the data analysis notebook."""
    house_df = pd.read_csv(path)

    house_df['grades_raw'] = house_df.grades
    house_df['grades'], house_df['grade_format'] = standardize_grades(house_df.grades_raw)
    house_df['grades'] = house_df.grades.fillna(house_df.grades.mean())

    house_df['international_bin'] = (house_df.international == 'international').astype(int)
    house_df['age_group'] = np.where(house_df.age < 25, 'under 25', '25 or older')

    return house_df
