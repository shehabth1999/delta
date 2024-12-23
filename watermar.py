from PIL import Image, ImageDraw, ImageFont

def create_repeating_watermark(text="Delta", output="repeating_watermark.png"):
    # Dimensions for the watermark
    canvas_width, canvas_height = 800, 800  # Adjust as needed for the output size
    watermark_size = 100  # Adjust the size of each watermark
    spacing = 50  # Spacing between watermarks

    # Create a transparent image for the canvas
    canvas = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(canvas)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", watermark_size // 2)  # Font size half of watermark size
    except IOError:
        font = ImageFont.load_default()

    # Create the watermark in a pattern
    for y in range(0, canvas_height, watermark_size + spacing):
        for x in range(0, canvas_width, watermark_size + spacing):
            # Add text at each grid point
            draw.text((x, y), text, font=font, fill=(255, 255, 255, 100))  # Semi-transparent white

    # Save the repeating watermark pattern
    canvas.save(output)
    print(f"Repeating watermark image saved as {output}")

# Generate the watermark
create_repeating_watermark()
