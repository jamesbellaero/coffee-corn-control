# coffee-corn-control
Ill-fated attempt to not electrocute myself with a popcorn maker.

## Use
The idea is that you setup a few relays on the gpio pins of a raspberry pi and switch between them to control which circuit is active. This works for any system with relays that run on GPIO pins, although the pins are hardcoded.

If you are lazy enough to not write your own garbage networking code, this stuff works fine for sending numbers from one console on your pc to another on your pi. Be sure to set the ip addresses to your own hardware. Run the client on the client pc and the other file on your pi.

## Hardware
Poplite popcorn popper: https://www.amazon.com/gp/product/B00006IUWA/ref=ppx_yo_dt_b_asin_title_o02_s01?ie=UTF8&psc=1
5v Relay Module: https://www.amazon.com/gp/product/B09G6H7JDT/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1

I could probably make a wiring diagram, but I'm lazy. If you want to know how to not electrocute yourself, create an issue.