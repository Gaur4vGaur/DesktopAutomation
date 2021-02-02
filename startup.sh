cd ~/1My/study/projects/python/DesktopAutomation
export PYTHONPATH="${PYTHONPATH}:."
gnome-terminal -- python3 processor/publication_controller.py
sleep 1
chromium-browser http://localhost:5000/publications/
