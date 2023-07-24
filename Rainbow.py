import socket
import time
import colorsys
num_leds = 85

def flatten(l):
    return [item for sublist in l for item in sublist]

def send_to_led(led):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    data = bytes(flatten(led))
    for i in range(3):
        sock.sendto(data, ("192.168.2.69", 1234))
        #time.sleep(0.1)
    sock.close()


def main():
    leds = []
    offset = 0
    k = 200
    while True:
        leds = []
        for i in range(num_leds):
            led = list(map(lambda x: int(x * 255),colorsys.hsv_to_rgb(((i + offset) % k)/k,1,0.2)))
            leds.append(led)
        send_to_led(leds)
        time.sleep(0.1)
        offset += 1


if __name__ == "__main__":
    main()