SPEED = 10.44 #this Usain Bolt´s speed in m/sec

def main():
    time_str = input ("Tell me run time (in secs): ")
    time_float = float(time_str)
    distance = round(time_float * SPEED,2)
    print(f"Usain Bolt can run {distance} meters")

if __name__ == "__main__":
    main()