# 16xTextureSplitter

A small and simple Python script for splitting Minecraft (or any .png) textures into 16x16 pixel tiles.

Useful when creating (Minecraft) textures that are larger than 16x16 and need to be separated into individual texture files.

## Features

* Splits PNG textures into 16x16 tiles
* Supports textures up to 64x64
* Automatically handles different texture sizes
* `16x32` textures are split into `_top` and `_bottom`
* `32x16` textures are split into `_left` and `_right`
* Larger textures are numbered automatically
* Skips textures that are already 16x16
* Skips textures larger than 64x64
* Skips textures whose dimensions are not divisible by 16
* Automatically creates an `output` folder

## Requirements

* Python 3
* Pillow

## Screenshot
<img width="720" height="400" alt="grafik" src="https://github.com/user-attachments/assets/e624a382-fa36-469e-abc9-d164faadeeaf" />


Install Pillow with:

```bash
pip install Pillow
```

## Usage

Place `texture_splitter.py` in the same folder as your PNG textures:

```text
texture-splitter/
├── texture_splitter.py
├── flower.png
├── plant.png
├── large_texture.png
└── output/
```

Run the script:

```bash
python texture_splitter.py
```
(or double click it)

The generated textures will be placed inside the `output` folder.

### Example

A `16x32` texture:

```text
flower.png
```

becomes:

```text
output/
├── flower_top.png
└── flower_bottom.png
```

A `32x16` texture:

```text
plant.png
```

becomes:

```text
output/
├── plant_left.png
└── plant_right.png
```

A `32x32` texture:

```text
large_texture.png
```

becomes:

```text
output/
├── large_texture_1.png
├── large_texture_2.png
├── large_texture_3.png
└── large_texture_4.png
```

## License

Feel free to use, modify, and redistribute this script.
