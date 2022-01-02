import subprocess


def get_repos():
    pass


def get_repo_name(url):
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
    repo_name = get_repo_name(root)

    print("=" * 80)
    # Init repository
    subprocess.run(
        f"cfgnet init {repo_name}", shell=True, executable="/bin/bash"
    )
    # Visualize repository
    subprocess.run(
        f"cfgnet export --output=graph --format=png --include-unlinked --visualize-dot {repo_name}", shell=True,
        executable="/bin/bash"
    )
    print("=" * 80)


def main():
    """Run the analysis."""

    # Init and export all repositories one by one
    for repo_root in get_repos():
        process_repo(root=repo_root)


if __name__ == "__main__":
    main()
