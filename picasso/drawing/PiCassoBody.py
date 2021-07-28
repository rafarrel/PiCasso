# @author Drew Meyers
from RPi.GPIO import GPIO
import time

class PiCasso:
    #default pin layout
    default_pins = {
        "x_on" : 4,
        "y_on" : 27,
        "h_on" : 13,
        "brd0" : 17,
        "brd1" : 18,
        "s0" : 12,
        "s1" : 6,
        "s2" : 5,
        "s3" : 3,
        "s4" : 24,
        "s5" : 23,
        "s6" : 22,
        "d0" : 12,
        "d1" : 6,
        "d2" : 5,
        "d3" : 3,
        "d4" : 24,
        "d5" : 23,
        "d6" : 22,
        "dir" : 20,
        "step" : 21,
        "m0" : 26,
        "m1" : 19,
        "m2" : 16,
    }

    #Motor stepping and speed dictionaries
    step_size = {
        'full' : (False, False, False),
        'half' : (True, False, False),
        'quarter' : (False, True, False),
        'eight' : (True, True, False),
        'sixteen' : (False, False, True),
        'thirtytwo' : (True, True, True),
    }

    speeds = {
        'max' : .0625,
        '3/4' : .08,
        '2/3' : .1,
        '1/2' : .125,
    }

    heads = []
    #Instance variables
    pins = {}
    axii = ['y0','y1','x','h']
    sense_axis = []

    motors = [
        ['y0',0,350, pins['y_on']],
        ['y1',0,350, pins['y_on']],
        ['x',0,400, pins['x_on']],
        ['h',0,5 pins['h_on']],
    ]


    def __init__(self, pins):
        for p in default_pins:
            if p not in pins:
                raise SystaxError
        self.pins = pins

        #Initialize pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for pin in pins:
            type = get_pin_type(pin)
            if type == 'sense':
                GPIO.setup(pins[pin], GPIO.IN)
            else:
                GPIO.setup(pins[pin], GPIO.OUT)

        #Send all axii home
        home()

    def get_pin_type(pin):
        if any(id in pin for id in ['x','y','h']):
            return 'ctrl'
        elif 'brd' in pin:
            return 'board'
        elif 'step' in pin:
            return 'step'
        elif 's' in pin:
            return 'sense'
        elif 'dir' in pin:
            return 'display'
        elif 'd' in pin:
            return 'dir'
        elif 'm' in pin:
            return "step_size"
        else:
            return 'unknown'


    def add_head(self, name, r, g, b, a, index=None):
        pop_head(name)
        if index:
            heads.insert(index, [name, r, g, b, a])
        else:
            heads.append([name, r, g, b, a])

    def pop_head(self, name):
        for h in range(len(heads)): #Check for duplicate
            if name in heads[h]:
                return heads.pop(h)
        return None


    def home(self):
        #go(0,0,'half', 15) #go to 0,0 at half stepping number of mm a second
        while not get_sense('x_home') and not get_sense('y_home'):
            if not get_sense('x_home'):
                send_pulse()

    def print_rbga(self, rgba_list):
        head_pixels = []
        for pixel_list in rgba_list:
            for pixel in pixel_list:
                head_pixels.append(determine_head_color(pixel, heads))

        for head in heads:
            image_map = []
            for pixel in head_pixels:
                if head[0] in pixel: #Match based on head name
                    image_map.append(1)
                else:
                    image_map.append(0)
            print_color(image_map, head[0])

    def determine_head_color(rgba, heads):
        best_head_r = None
        best_head_g = None
        best_head_b = None
        best_head_a = None
        r_dif = 256
        g_dif = 256
        b_dif = 256
        a_dif = 256

        for head in heads:
            if head[1] - rgba[0] < r_dif:
                best_head_r = head[0]
                r_dif = head[1] - rgba[0]
            if head[2] - rgba[1] < r_dif:
                best_head_g = head[0]
                g_dif = head[2] - rgba[1]
            if head[3] - rgba[2] < r_dif:
                best_head_b = head[0]
                b_dif = head[3] - rgba[2]
            if head[4] - rgba[3] < r_dif:
                best_head_a = head[0]
                a_dif = head[4] - rgba[3]

        #Find a close match
        if best_head_r == best_head_g and best_head_r == best_head_b:
            return best_head_r
        elif best_head_b == best_head_g and best_head_b == best_head_r:
            return best_head_b
        elif elif best_head_g == best_head_b and best_head_g == best_head_r:
            return best_head_g

        #If none are close, assign black
        return heads[0][0]



    def print(self, image_map):
        for head in heads:
            print_color(image_map, head)

    def print_color(self, image_map, head_name):
        pixel_counter = 0
        color_map = []
        for row in image_map:
            row_map = []
            for pixel in row:
                if is_correct_head(pixel, head_name):
                    row_map.append(1)
                else:
                    row_map.append(0)
            color_map.append(row_map)

        for row in range(size(color_map)):
            for col in range(size(color_map[row])):
                if paint_value == 1:
                    go(row, col, 'full', get_head())



    def print_picode(self, picode):
        for line in picode:
            line_str = line.split(',')
            go(line_str[0],line_str[1],line_str[2], line_str[3])


    def go(self, x,y, step_size, speed,head=False):
        #Direction changes from current head position
        x_change = get_x-x
        y_change = get_y-y

        set_dir(x_change < 0, 'x')
        set_dir(y_change < 0, 'y')

        x_pulses = get_motor_pulse(abs(x_change))
        y_pulses = get_motor_pulse(abs(y_change))

        if x_change > y_change:
            for x in range(x_change):
                send_pulse(motors['x'],speed[speed])

        if head:
            set_head(not get_head)


    def set_dir(self, dir, axis):
        GPIO.output(axis, dir)

    def set_head(self, position):
        if not (position and get_head):
            set_dir(position,'h')
            motor_move(.25, 'h', step_size['half'], speeds['max'])

    def motor_move(self, rotation, motor, step_size, speed):
        steps = rotation * 200


    def send_pulse(self, pin, speed):
        GPIO.output(pin, GPIO.HIGH)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(speeds[speed])

    def send_pulses(self, pulses, pin, steps, speed):
        for pulse in pulses:
            send_pulse(pin, speed)

    def update_coord(self, axis, amount):
        self.positions[axis].value() = get_axis(axis)+amount

    def get_axis_theo(self, axis):
        return self.positions[axis].value()[0]

    def get_axis_actual(self, axis):
        return self.positions[axis].value()[1]

    def get_x(self):
        return self.get_axis_theo('x')
    def get_y0(self):
            return self.get_axis_theo('y0')
    def get_y1(self):
            return self.get_axis_theo('y1')
    def get_head(self):
            return self.get_axis_theo('h')

    #Get the raw binary output of the sensor board
    def get_sensor_string(self):
        sense_str = ''
        for pin in input_pins:
            sensor_val = GPIO.input(pin)
            if sensor_val:
                sense_str += '1'
            else:
                sense_str += '0'
        return sense_str

    def check_start_stop():
        return GPIO.input('start_stop') == GPIO.HIGH
