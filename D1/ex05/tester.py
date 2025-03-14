from load_image import ft_load
from pimp_image import ft_invert,ft_red, ft_green, ft_blue, ft_grey, display_image

array = ft_load("landscape.jpg")

display_image(array, "Figure VIII.1: Original")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

print(ft_invert.__doc__)
print(ft_red.__doc__)
print(ft_green.__doc__)
print(ft_blue.__doc__)
print(ft_grey.__doc__)
