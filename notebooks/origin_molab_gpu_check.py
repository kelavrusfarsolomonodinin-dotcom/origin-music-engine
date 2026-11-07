import marimo

__generated_with = "0.19.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import platform
    import shutil
    import subprocess
    import sys
    import marimo as mo
    return mo, platform, shutil, subprocess, sys


@app.cell
def _(mo, platform, shutil, sys):
    free_gb = shutil.disk_usage("/").free / (1024 ** 3)
    return mo.md(
        f"""# ORIGIN MUSIC ENGINE — проверка облачного GPU

Сейчас проверяем только облачную среду. Музыкальная модель пока не устанавливается.

- **Python:** {sys.version}
- **Платформа:** {platform.platform()}
- **Свободное место:** {free_gb:.1f} ГБ
"""
    )


@app.cell
def _(mo, subprocess):
    try:
        result = subprocess.run(
            ["nvidia-smi"],
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
        if result.returncode == 0:
            message = "## GPU обнаружен\n\n" + result.stdout
        else:
            details = result.stderr or result.stdout or "nvidia-smi не вернул данных"
            message = "## GPU пока не подключён\n\n" + details
    except Exception as exc:
        message = "## GPU не обнаружен\n\n" + f"Команда nvidia-smi недоступна: {exc}\n\nПроверим подключение GPU в настройках блокнота."
    return mo.md(message)


if __name__ == "__main__":
    app.run()
