from PIL import Image, ImageDraw, ImageFont


def asciiartify(imagename: str, resize_width: int, scale_combine: int) :
  img = Image.open(imagename)

  # Convert the image to grayscale
  img = img.convert("L")

  # Resize the image
  if resize_width:
    new_width = resize_width
  else:
    new_width = width
  width, height = img.size
  new_height = int((height / width) * new_width)
  img = img.resize((new_width, new_height))

  # Define the symbols to use
  symbols = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

  # Divide the image into a grid of cells
  cell_size = scale_combine
  num_cells_x = int(new_width / cell_size)
  num_cells_y = int(new_height / cell_size)

  # Compute the average brightness of each cell and map it to a symbol
  symbol_img = Image.new("L", (new_width, new_height), color=255)
  symbol_draw = ImageDraw.Draw(symbol_img)
  font = ImageFont.truetype("Arial.ttf", size=cell_size)

  for y in range(num_cells_y):
      for x in range(num_cells_x):
          cell_left = x * cell_size
          cell_top = y * cell_size
          cell_right = cell_left + cell_size
          cell_bottom = cell_top + cell_size
          cell_box = (cell_left, cell_top, cell_right, cell_bottom)
          cell_img = img.crop(cell_box)
          cell_brightness = sum(cell_img.getdata()) / (cell_size * 
cell_size)
          symbol_index = int((cell_brightness / 255) * (len(symbols) - 1))
          symbol = symbols[symbol_index]
          symbol_draw.text((cell_left, cell_top), symbol, fill=0, 
font=font)

  return symbol_img

imagename = "EMMA WATSON.jpg"
symbol_img = asciiartify(imagename, 1200, 10)
symbol_img.save(f"{imagename.split('.')[0]}_converted.jpg")
