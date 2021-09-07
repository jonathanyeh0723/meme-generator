import subprocess
import os


if __name__ == "__main__":
    #result = subprocess.call(["ls", "-lt", "./static"])
    #print(result)
    #print(type(result))
    #print(type(result))
    #print(len(result))
    #print(os.listdir('./static'))
    #print(os.listdir('./static')[-1])
    result = subprocess.call(["ls -lt ./static > images.txt"], shell=True)
    with open('images.txt', 'r') as f:
        for line in f:
            if line.startswith('-'):
                last_img = line.split(' ')[-1]
                break
    print(last_img)
    print(type(last_img))
