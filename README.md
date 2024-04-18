mamba create -n mamba-template python=3.12
conda config --add channels conda-forge
conda config --set channel_priority strict

# Setup Ruff
# install the VSCode extension so Ruff can be configured via .vscode/settings.json, you can check that it is using the correct Ruff binary by checking the Ruff logs in the Output tab
mamba install ruff      




# Jupyter notebook setup
mamba install jupyterlab_code_formatter jupyterlab jupyterlab_vim
To setup Jupyter Notebook with Ruff
https://gist.github.com/jbwhit/eecdd1cac2756df85ad165f437445b0b



# Mypy VSCode setup
mamba install mypy
Install MS VSCode extension

# pytest setup
mamba install pytest pytest-watch

# install pre-commit
mamba install pre-commit && pre-commit install