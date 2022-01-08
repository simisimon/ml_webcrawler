import subprocess
import os
import glob
import pandas as pd
import subprocess

# The folder where we store our results.
EVALUATION_FOLDER = "out"


def get_repo_name_from_url(url):
    """
    Analyze a repository with CfgNet.
    :param url: URL to the repository
    :return: Repository name
    """
    repo_name = url.split("/")[-1]
    repo_name = repo_name.split(".")[0]
    return repo_name


def process_repo(root):
    """
    Analyze a repository with CfgNet.
    :param url: URL to the repository
    :param commit: Hash of the lastest commit that should be analyzed
    :param ignorelist: List of file paths to ignore in the analysis
    """
    repo_name = get_repo_name_from_url(url)
    repo_folder = EVALUATION_FOLDER + "/" + repo_name
    results_folder = EVALUATION_FOLDER + "/results/" + repo_name
    abs_repo_path = os.path.abspath(repo_folder)

    print("=" * 80)

    # Init repository
    subprocess.run(
        f"cfgnet init {root}", shell=True, executable="/bin/bash"
    )

    # Visualize repository
    #subprocess.run(
    #    f"cfgnet export --output=graph --format=png --include-unlinked --visualize-dot {repo_name}", shell=True,
    #    executable="/bin/bash"
    #)

    print("=" * 80)


def main():
    """Run the analysis."""

    df = pd.read_csv("scikit_learn_repos.csv")

    TEST_REPOS = df["repo_url"]

    """Run the analysis."""
    # create evaluation folder
    if os.path.exists(EVALUATION_FOLDER):
        subprocess.run(["rm", "-rf", EVALUATION_FOLDER])
    subprocess.run(["mkdir", "-p", EVALUATION_FOLDER + "/results"])

    index = int(sys.argv[1])
    process_repo(TEST_REPOS[index])

if __name__ == "__main__":
    main()
