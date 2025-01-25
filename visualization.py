# Jitong Zou
# DS5110
# January 24, 2025

import pandas as pd
import matplotlib.pyplot as plt

# Function to load data from a CSV file
def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    return pd.read_csv(file_path)

# Function to calculate statistical metrics
def calculate_statistics(data, numerical_columns, species_column):
    """
    Calculate and print statistical metrics (mean, median, variance, standard deviation)
    for the entire dataset and for each species group.

    Parameters:
        data (pd.DataFrame): The dataset.
        numerical_columns (list): List of numerical columns to calculate statistics for.
        species_column (str): The column indicating species.

    Returns:
        None
    """
    print("Statistical Summary:")
    for column in numerical_columns:
        print(f"\nStatistics for {column}:")
        print("Overall:")
        print(f"  Mean: {data[column].mean():.2f}")
        print(f"  Median: {data[column].median():.2f}")
        print(f"  Variance: {data[column].var():.2f}")
        print(f"  Standard Deviation: {data[column].std():.2f}")

        species_stats = data.groupby(species_column)[column].agg(['mean', 'median', 'var', 'std'])
        print("By Species:")
        print(species_stats)

# Function to plot histograms
def plot_histograms(data, numerical_columns, species_column):
    """
    Plot histograms for numerical columns, including overall distribution and species-specific distributions.

    Parameters:
        data (pd.DataFrame): The dataset.
        numerical_columns (list): List of numerical columns to plot.
        species_column (str): The column indicating species.

    Returns:
        None
    """
    species = data[species_column].unique()
    for column in numerical_columns:
        plt.figure(figsize=(10, 8))
        plt.suptitle(f'{column} Distribution', fontsize=16)

        # Overall distribution
        plt.subplot(2, 2, 1)
        plt.hist(data[column], bins=15, edgecolor='black', alpha=0.7)
        plt.title('All')
        plt.xlabel(column)
        plt.ylabel('Count')

        # Species-specific distributions
        for i, specie in enumerate(species, start=2):
            plt.subplot(2, 2, i)
            specie_data = data[data[species_column] == specie]
            plt.hist(specie_data[column], bins=15, edgecolor='black', alpha=0.7)
            plt.title(specie)
            plt.xlabel(column)
            plt.ylabel('Count')

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()

# Function to plot boxplots
def plot_boxplots(data, numerical_columns, species_column):
    """
    Plot boxplots for numerical columns, showing overall and species-specific distributions.

    Parameters:
        data (pd.DataFrame): The dataset.
        numerical_columns (list): List of numerical columns to plot.
        species_column (str): The column indicating species.

    Returns:
        None
    """
    species = data[species_column].unique()
    for column in numerical_columns:
        plt.figure(figsize=(10, 6))
        plt.title(f'{column} Distribution (Boxplot)', fontsize=16)

        # Prepare data for boxplot
        all_data = [data[column]]
        species_data = [data[data[species_column] == specie][column] for specie in species]
        all_data.extend(species_data)

        # Set labels
        labels = ['All'] + list(species)

        # Plot boxplot
        plt.boxplot(all_data, labels=labels, patch_artist=True, showmeans=True)
        plt.xlabel('Species', fontsize=12)
        plt.ylabel(column, fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        plt.show()

# Function to plot scatter plots
def plot_scatter(data, x_column, y_column, species_column):
    """
    Plot scatter plots to visualize the relationship between two numerical columns,
    with points colored by species.

    Parameters:
        data (pd.DataFrame): The dataset.
        x_column (str): The column to plot on the x-axis.
        y_column (str): The column to plot on the y-axis.
        species_column (str): The column indicating species.

    Returns:
        None
    """
    species = data[species_column].unique()
    colors = ['blue', 'orange', 'green']

    plt.figure(figsize=(10, 6))
    plt.title(f'{x_column} vs {y_column} (Scatter Plot)', fontsize=16)

    # Plot species-specific scatter points
    for specie, color in zip(species, colors):
        specie_data = data[data[species_column] == specie]
        plt.scatter(specie_data[x_column], specie_data[y_column], label=specie, color=color, alpha=0.7, edgecolors='k')

    # Add legend and labels
    plt.xlabel(x_column, fontsize=12)
    plt.ylabel(y_column, fontsize=12)
    plt.legend(title='Species')
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.show()

# Main program
if __name__ == "__main__":
    # File path
    file_path = './data/plant.csv' # data/plant.csv

    # Load data
    plant_data = load_data(file_path)

    # Define columns
    numerical_columns = ['LeafWidth', 'LeafLength']
    species_column = 'PlantName'
    x_column = 'LeafLength'
    y_column = 'LeafWidth'

    # Calculate statistics
    calculate_statistics(plant_data, numerical_columns, species_column)

    # Generate plots
    plot_histograms(plant_data, numerical_columns, species_column)
    plot_boxplots(plant_data, numerical_columns, species_column)
    plot_scatter(plant_data, x_column, y_column, species_column)
