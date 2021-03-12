import sys

if len(sys.argv) != 2:
	sys.exit('Please give a quantum.')
else:
	quantum = int(sys.argv[1])


def FCFS(seq):

	schedule = []
	turnaround_times = []

	for i in range(len(seq)):
		if i == 0:
			turnaround_times.append(seq[0])
		else:
			turnaround_times.append(turnaround_times[i-1] + seq[i])

		schedule.append((i, seq[i]))

	pretty_print(schedule, turnaround_times)


def SJF(seq):

	schedule = []
	turnaround_times = []

	seq = sorted(seq)     # sort the sequence to get the schedule

	for i in range(len(seq)):
		if i == 0:
			turnaround_times.append(seq[0])
		else:
			turnaround_times.append(turnaround_times[i-1] + seq[i])

		schedule.append((i, seq[i]))

	pretty_print(schedule, turnaround_times)


def SRTF(seq):

	schedule = []
	turnaround_times = []

	# assuming the scheduler receives a new process every second
	# we implement this 'receiving' since SRTF where the scheduler sees all processes at once is just SJF
	# so, the TAT of the process starts when the process is 'received', not at t=0 like the other algorithms

	current_process = 0      # id of the currently running process
	new_process = 0
	remaining_times = []


	while True:

		if new_process < len(seq):
			remaining_times.append(seq[new_process])     # the scheduler 'receives' a new process, with an expected runtime
			turnaround_times.append(1)
			new_process += 1

		if any(remaining_times):

			current_process = non_zero_min(remaining_times)   # discard processes with remaining time = 0
			remaining_times[current_process] -= 1

			try:
				if schedule[-1][0] == current_process:        # check if the new current process was the one scheduled last; 
					schedule[-1][1] += 1					  # if so, add the new unit of time to the time of the previous slot
				else:
					schedule.append([current_process, 1])
			except IndexError:
				schedule.append([current_process, 1])

		else:           # if all remaining times are 0, stop 
			break

		# mark the passage of time in the turnaround times by incrementing the TAT of 
		# all processes managed by the scheduler (that is, processes that have been received by the scheduler, but aren't done)
		turnaround_times = list(map(lambda t: t[1]+1 if remaining_times[t[0]] > 0 else t[1], enumerate(turnaround_times)))
		

	pretty_print(schedule, turnaround_times)


def RR(seq):

	schedule = []
	turnaround_times = [0] * len(seq)
	remaining_times = seq[:]

	def find_next_process(current):
		# implements the 'roundness' of the Round Robin
		new_current = 0 if (current == len(seq) - 1) else current + 1
		return new_current
	
	current_process = 0
	while True:

		if any(remaining_times):
			process_slot = min(quantum, remaining_times[current_process])   # find out how long the current process will run (maximum quantum)
			
			
			try:
				if schedule[-1][0] == current_process:        # check if the new current process was the one scheduled last; 
					schedule[-1][1] += process_slot			  # if so, add the new slot to the previous slot
				else:
					schedule.append([current_process, process_slot])
			except IndexError:
				schedule.append([current_process, process_slot])
			
			#schedule.append([current_process, process_slot])

			turnaround_times = list(map(lambda t: t[1]+process_slot if remaining_times[t[0]] > 0 else t[1], enumerate(turnaround_times)))
			remaining_times[current_process] -= process_slot                # decrease its remaining time

			current_process = find_next_process(current_process)
			while remaining_times[current_process] == 0 and any(remaining_times):
				current_process = find_next_process(current_process)

		else:
			break


	pretty_print(schedule, turnaround_times)





def non_zero_min(list_):
	index, value = min(enumerate(list_), key=lambda x: x[1] if x[1] > 0 else float('inf'))
	return index

def pretty_print(sched, tat):
	print('Schedule: \n\t', '|'.join([" P{:<2}: {:<3}".format(i, t) for i, t in sched]))
	print('Turnaround times: \n\t', '|'.join([" P{:<2}: {:<3}".format(i, t) for i, t in enumerate(tat)]))


if __name__ == "__main__":

	d = {1: [5, 3, 12, 100, 1, 2, 3, 4, 5], 2: [5, 4, 3, 2, 1, 100, 12, 3, 5], 3: [23, 17, 31, 29, 71, 2, 5, 113]}
	seq = int(input('Which example sequence? (1, 2 or 3):\n'))
	seq = d[seq]

	print('Sequence: ', seq)
	print('Quantum (RR): ', quantum)

	print('\n###### First Come First Serve ######')
	FCFS(seq[:])

	print('\n###### Shortest Job First ######')
	SJF(seq[:])

	print('\n###### Shortest Remaining Time First ######')
	SRTF(seq[:])

	print('\n###### Round Robin ######')
	RR(seq[:])