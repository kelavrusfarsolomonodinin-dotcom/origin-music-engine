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
    mo.md("# ORIGIN MUSIC ENGINE — проверка облачного GPU\\n\\nСначала проверяем среду molab. Установка музыкальной модели начнётся только после подтверждения GPU.")
    mo.md(f"**Python:** {sys.version}\\n\\n**Платформа:** {platform.platform()}\\n\\n**Свободное место:** {shutil.disk_usage('/').free / 1024**3:.1f} ГБ")
    return

@app.cell
def _(mo, subprocess):
    try:
        result = subprocess.run(["nvidia-smi"], capture_output=True, text=True, timeout=20)
        if result.returncode == 0:
            mo.md("## GPU обнаружен\\n\\n" + result.stdout)
        else:
            mo.md("## GPU пока не подключён\\n\\n" + (result.stderr or result.stdout or "nvidia-smi не вернул данных"))
    except Exception as exc:
        mo.md(f"## GPU не обнаружен\\n\\nКоманда nvidia-smi недоступна: {exc}\\n\\nПроверим подключение GPU в настройках блокнота.")
    return

if __name__ == "__main__":
    app.run()
