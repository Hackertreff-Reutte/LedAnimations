import socket
import time
num_leds = 85

def flatten(l):
    return [item for sublist in l for item in sublist]

def send_to_led(led):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    data = bytes(flatten(led))
    for i in range(3):
        sock.sendto(data, ("255.255.255.255", 1234))
        time.sleep(0.1)
    sock.close()

def main():

    send_to_led([[255,255,255]*15])
    time.sleep(10)

    while True:
        led = []
        for i in range(num_leds):
            led.append([0,0,0])

        print("Study")
        for i in range(5):
            led[len(led) - ((i + 1) * 5)] = [0,255,0]
            send_to_led(led)
            print("Update Study")
            time.sleep(60*5)

        print("Pause")
        led = []
        for i in range(num_leds):
            led.append([0,0,60])
        send_to_led(led)
        time.sleep(20)

        print("Pause Countdown")
        for i in range(5):
            led[len(led) - ((i + 1) * 5)] = [255,0,0]
            send_to_led(led)
            time.sleep(60)

        print("Alert")
        led = []
        for i in range(num_leds):
            led.append([60,0,0])
        send_to_led(led)
        time.sleep(20)

if __name__ == "__main__":
    main()