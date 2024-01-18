import dearpygui.dearpygui as dpg
import serial
import yaml

ser = serial.Serial('COM3',115200,timeout=5)
VERSION = "0.0.1"
fingers_max = [0] * 5
fingers_min = [0] * 5

def init():
    with open('./config.yml', 'r', encoding='utf-8') as f:
        res = yaml.load(f.read(), Loader=yaml.FullLoader)


def save_callback():
    print("Save Clicked")


def serial_init():
    # Setting up the Serial
    global ser
    ser = ""

# Create the GUI
dpg.create_context()
with dpg.font_registry():
    with dpg.font("./fonts/simhei.ttf", 14, default_font=True) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
    dpg.bind_font(default_font)

dpg.create_viewport(title="Finger Extension Server " + VERSION, width=600, height=600)
dpg.setup_dearpygui()
with dpg.window(label="食指状态", width=180, height=60):
    # dpg.add_text(default_value="食指")
    # dpg.add_button(label="Save", callback=save_callback)
    # dpg.add_input_text(label="")
    dpg.add_slider_float()

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


