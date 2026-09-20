"""Shared constants, column groups and the plotting theme for INSTK5000 Project 1."""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

__all__ = [
    'PROJECT_DIR', 'DATA_PATH', 'FIG_DIR', 'RESULTS_DIR',
    'RANDOM_STATE', 'MARGIN', 'MARGIN_PERCENT',
    'target_column', 'decision_columns', 'decision_makers', 'algorithms', 'predictors',
    'sensitive_features', 'relevant_features', 'grey_zone_features',
    'numerical_features', 'categorical_features', 'continuous_features', 'feature_cols',
    'DIVERGING_CMAP', 'SEQUENTIAL_CMAP', 'BINARY_PALETTE',
    'PRIMARY_COLOR', 'SECONDARY_COLOR', 'MARGIN_COLOR',
    'set_project_theme',
]

PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / 'data.csv'
FIG_DIR = PROJECT_DIR / 'figures'
RESULTS_DIR = PROJECT_DIR / 'results'
FIG_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)

RANDOM_STATE = 0
MARGIN = 0.05
MARGIN_PERCENT = 5.0

target_column = 'should_recieve_housing'
decision_columns = ['HO', 'A1', 'A2', 'A3', 'A4']
decision_makers = ['HO', 'A1', 'A2', 'A3', 'A4']
algorithms = ['A1', 'A2', 'A3', 'A4']
predictors = ['HO', 'A1', 'A2', 'A3', 'A4']

sensitive_features = ['age', 'international']
relevant_features = ['commute_distance_km', 'financial_need_score', 'housing_urgency_rating']

# grades and semesters_completed are in a grey zone. They are not sensitive by themselves,
# but grades is a proxy for international (see the tidying part) and semesters_completed is
# strongly connected to age, so both can leak sensitive information into a decision.
grey_zone_features = ['grades', 'semesters_completed']

numerical_features = ['age', 'commute_distance_km', 'financial_need_score', 'housing_urgency_rating', 'grades']
categorical_features = ['international', 'semesters_completed', 'should_recieve_housing', 'HO', 'A1', 'A2', 'A3', 'A4']
continuous_features = ['financial_need_score', 'housing_urgency_rating', 'commute_distance_km', 'grades']
feature_cols = ['age', 'semesters_completed', 'commute_distance_km',
                'financial_need_score', 'housing_urgency_rating', 'grades']

DIVERGING_CMAP = 'vlag'
SEQUENTIAL_CMAP = 'rocket_r'
BINARY_PALETTE = {0: '#9FB1C1', 1: '#C44E52'}
PRIMARY_COLOR = '#4C72B0'
SECONDARY_COLOR = '#DD8452'
MARGIN_COLOR = '#C44E52'


def set_project_theme():
    """One theme for every notebook, so all the figures in the report look the same."""
    sns.set_theme(style='whitegrid', context='notebook', palette='deep')
    plt.rcParams.update({
        'figure.dpi': 110,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'axes.titlesize': 12,
        'axes.titleweight': 'bold',
        'axes.labelsize': 10,
        'axes.edgecolor': '#666666',
        'grid.color': '#DDDDDD',
        'grid.linewidth': 0.6,
        'legend.frameon': False,
    })
