#!/usr/bin/env python3

from envirophat import light, weather
from argh import *


def convert_to_farenheit(temperature):
    return round(1.8*temperature + 32, 2)


def get_tempf():
    return convert_to_farenheit(weather.temperature())


def get_tempc():
    return weather.temperature()

def main():
    parser = ArghParser()
    parser.add_commands([get_tempf, get_tempc, light.light, light.rgb])
    parser.dispatch()

if __name__ == '__main__':
    main()
