# My PySpark Project

## Prerequisites

### 1. Install Java
PySpark requires Java to run. Ensure you have **Java Development Kit (JDK)** installed.

1. Download and install the JDK from [here](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
2. Set the `JAVA_HOME` environment variable:
   - **Windows**:
     - Open **Environment Variables** > **System Variables**.
     - Create a new variable `JAVA_HOME` with the value pointing to your JDK installation folder (e.g., `C:\Program Files\Java\jdk-11.0.11`).
     - Add `%JAVA_HOME%\bin` to your **Path**.

### 2. Install Spark and winutils (For Windows)

1. Download **Apache Spark**:
   - Download from the [Apache Spark website](https://spark.apache.org/downloads.html) and extract it to a directory (e.g., `C:\spark`).
   
2. Download **winutils.exe** (for Windows users):
   - Go to [winutils GitHub repository](https://github.com/steveloughran/winutils) and download `winutils.exe` for your version of Hadoop.
   - Place `winutils.exe` in `C:\spark\bin`.

3. Set **SPARK_HOME** and **HADOOP_HOME** environment variables:
   - Set the `SPARK_HOME` variable to the Spark installation path (e.g., `C:\spark`).
   - Set the `HADOOP_HOME` variable to the same path as `SPARK_HOME`.
   - Add `%SPARK_HOME%\bin` and `%HADOOP_HOME%\bin` to your **Path** environment variable.

### 3. Install Anaconda (Python Environment)

1. Download and install **Anaconda** from [here](https://www.anaconda.com/products/individual).
2. Create a Conda environment for PySpark:

   ```bash
   conda create --name myenv python=3.9
   conda activate myenv

4. configure vscode to conda env :
Open Command Palette (Ctrl+Shift+P) and search for Preferences: Open Settings (JSON).
Add this to the file:

"python.defaultInterpreterPath": "C:\\Users\\Sakshi\\anaconda3\\envs\\myenv\\python.exe",
"python.condaPath": "C:/ProgramData/Anaconda3/Scripts/conda.exe"

5. Set Pyspark Env Vars : (use command "where python" to find the path)

export PYSPARK_PYTHON="C:/ProgramData/Anaconda3/envs/myenv/python.exe"
export PYSPARK_DRIVER_PYTHON="C:/ProgramData/Anaconda3/envs/myenv/python.exe"


Project Setup:


1. Clone the repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt

3. To Install project as a package

pip install -e .

4. To run unit tests:

pytest tests/

5.Install pre-commit hooks:
create 2 files (pre-push & pre-commit) in .git->hooks folder

add pre-commit hooks in pre-push file
  

5. Orchestration : Dagster web UI

dagit -w dagster_project/workspace.yaml

localhost:3000 (open in browser)



------------------------------------------

6. Steps to setup the conda environment 

conda create --name myenv python=3.9
conda init and restart vscode
conda activate myenv
pip install -r requirements.txt



7. For jupyter notebook, follow  these:
conda install ipykernel
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"

#test