import ControlManual

cm = ControlManual.Client()

while True:
    i = input(f'{cm.getpath()} >> ')
    cmd = cm.instance(i)
    print(cmd)