#Day 07

import string

with open('./07.txt') as myinput:
    inputlines = myinput.readlines()

steps = {line.split()[7]: [line.split()[1]] for line in inputlines}

for line in inputlines:
    step, required_step = line.split()[7], line.split()[1]
    if required_step not in steps.keys():
        steps[required_step] = False
    if required_step not in steps[step]:
        steps[step] += required_step

steps = dict(sorted(steps.items()))

#Part 1

order_of_steps = []

def get_order_of_steps(steps, order_of_steps):
    for step, required_steps in steps.items():
        if step not in order_of_steps:
            if not required_steps or all(required_step in order_of_steps for required_step in required_steps):
                order_of_steps.append(step)
                return get_order_of_steps(steps, order_of_steps)

get_order_of_steps(steps, order_of_steps)

print(''.join(order_of_steps))

#Part 2

time_required = list(enumerate(string.ascii_uppercase, 61))

table = [['.'] for worker in range(5)] + [[]]

def check_step_completion(worker_current_step, step, time_req, worker_num, done):
    if step == worker_current_step:
        if worker_num.count(worker_current_step) == time_req:
            if worker_current_step not in done:
                done += worker_current_step
            worker_num += '.'
        else:
            worker_num += worker_current_step

def get_sleigh_construction_time(second, steps, table):
    worker_1, worker_2, worker_3, worker_4, worker_5, done = table
    for (time_req, step) in time_required:
        check_step_completion(worker_1[-1], step, time_req, worker_1, done)
        check_step_completion(worker_2[-1], step, time_req, worker_2, done)
        check_step_completion(worker_3[-1], step, time_req, worker_3, done)
        check_step_completion(worker_4[-1], step, time_req, worker_4, done)
        check_step_completion(worker_5[-1], step, time_req, worker_5, done)
    for step, required_steps in steps.items():
        if step not in worker_1 + worker_2 + worker_3 + worker_4 + worker_5:
            if not required_steps or all(required_step in done for required_step in required_steps):
                if worker_1[-1] == '.':
                    worker_1[-1] = step
                elif worker_2[-1] == '.':
                    worker_2[-1] = step
                elif worker_3[-1] == '.':
                    worker_3[-1] = step
                elif worker_4[-1] == '.':
                    worker_4[-1] = step
                elif worker_5[-1] == '.':
                    worker_5[-1] = step
    if len(done) < len(order_of_steps):
        return get_sleigh_construction_time(second + 1, steps, table)
    else:
        return second

print(get_sleigh_construction_time(0, steps, table))