import subprocess
import os


def test_model_training():
    script_path = os.path.abspath(os.path.join("..", "train.py"))
    project_root = os.path.abspath("..")

    result = subprocess.run(["python", script_path], cwd=project_root)

    assert result.returncode == 0, "Training script failed!"
