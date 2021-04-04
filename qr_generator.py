#
# Usage
# ===============
# terminal:
#
# myqr words
# [-h]
# [-v {1,2,3,...,40}]
# [-l {L, M, Q, H}]
# [-p image_filename]
# [-c]
# [-con contrast_value]
# [-bri brightness_value]
# [-n output_filename]
# [-d output_directory]


from MyQR import myqr

version, level, qr_name = myqr.run(
    words="Hello, I am LiShun, nice to meet you!",
    version=10,
    level='H',
    picture="cube.jpg",
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name=None,
    # save_dir=os.getcwd()
)
