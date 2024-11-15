import time
import sys

done = False
def animate():
    while done == False:
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(1)
    sys.stdout.write('\rDone!')

animate()
done = False