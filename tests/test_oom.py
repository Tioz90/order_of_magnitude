from order_of_magnitude import order_of_magnitude

print("Order of magnitude:", order_of_magnitude.order_of_magnitude([1.1e-24, 100e3, 0]))
print("Power of ten:", order_of_magnitude.power_of_ten([1.1e-24, 100e3, 0]))
print("Prefix:", order_of_magnitude.prefix([1.1e-24, 100e3, 0]))
print("Symbol:", order_of_magnitude.symbol([1.1e-24, 100e3, 0]))
print("Only symbol:", order_of_magnitude.symbol([1.1e-24, 100e3, 0], omit_x=True))
print("Prefix in words:", order_of_magnitude.prefix([1.1e-24, 100e3, 0], word=True))
print("Only prefix in words:", order_of_magnitude.prefix([1.1e-24, 100e3, 0], omit_x=True, word=True))
print("Short scale:", order_of_magnitude.short_scale([1.1e-24, 100e3, 0]))
print("Short scale in numbers:", order_of_magnitude.short_scale([1.1e-24, 100e3, 0], word=False))
print("Long scale only OOM:", order_of_magnitude.long_scale([1.1e-24, 100e3, 0], omit_x=True))
print("Long scale dictionary", order_of_magnitude.long_scale_dict())
