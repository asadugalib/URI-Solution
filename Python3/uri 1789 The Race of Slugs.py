#1789 The Race of Slugs

while True:
    try:
        num_of_slugs = int(input())
        if 1 <= num_of_slugs <= 500:
            speed = list(map(int, input().split()[:num_of_slugs]))
            max_speed = max(speed)
            min_speed = min(speed)
            if max_speed <= 50 and min_speed >= 1:
                if max_speed >= 20:
                    print("3")
                elif 10 <= max_speed < 20:
                    print("2")
                else:
                    print("1")
    except:
        break
