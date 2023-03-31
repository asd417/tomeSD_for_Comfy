# CheckpointTomeLoader
tomeSD(https://github.com/dbolya/tomesd) applied to ComfyUI stable diffusion UI using custom node

# Installation

Place tomeloader.py in ``\ComfyUI_windows_portable\ComfyUI\custom_nodes``

Open cmd at ``\ComfyUI_windows_portable\python_embeded\Lib\site-packages``

Clone the repository:
```bash
git clone https://github.com/dbolya/tomesd
cd tomesd
```
Then set up the tomesd package with:
```bash
python setup.py build develop
```

Copy contents of ``\ComfyUI_windows_portable\python_embeded\Lib\site-packages\tomesd\build\lib\tomesd``
to 
``\ComfyUI_windows_portable\python_embeded\Lib\site-packages\tomesd``
There's probably a better way to install but hey it works


# Tip

Adjust ratio. 0.5 is recommended. It's recommended that you do not increase the value above 0.5
