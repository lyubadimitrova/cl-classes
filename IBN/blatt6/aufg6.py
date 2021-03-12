import sys

if len(sys.argv) != 2:
	sys.exit('Number of frames ambiguous.')
else:
	num_frames = int(sys.argv[1])


def clock(sequence):
	r_bits = [0] * num_frames       # all R-bits are 0 in the beginning
	frames = ["E"] * num_frames     # all frames are empty in the beginning
	hand = 0                        # the clock hand (pointer)

	print('Starting memory state: ')
	print_mem_state(frames, r_bits, hand)


	def move_hand():
		nonlocal hand
		hand = 0 if (hand == num_frames -1) else hand + 1

	for fr_num in sequence:
		print('Accessing frame {}:'.format(fr_num))

		if fr_num in frames:						# if the frame is in memory
			print('... Already in memory.')
			r_bits[frames.index(fr_num)] = 1        # set the reference bit to 1; no need to move the hand
		
		else:                               		# if the frame is not in memory, we need to find free space/victim
			
			while r_bits[hand] == 1:                # move the hand until you find an R-bit set to 0                
				r_bits[hand] = 0                    # until then, turn all R-bits off
				move_hand()
													# after the loop, we've found either a free space or a victim
			frames[hand] = fr_num					# replace it with the new frame
			r_bits[hand] = 1						# set the bit
			move_hand()								# move the hand one field

		print('Memory state after: ')
		print_mem_state(frames, r_bits, hand)


def print_mem_state(frames, rbits, hand):

	frames[hand] = '*' + frames[hand]         # to also show where the hand is
	print(' '.join(("{:>2}({})".format(f, r) for f, r in zip(frames, rbits))), end='\n\n')
	frames[hand] = frames[hand].strip('*')


if __name__ == "__main__":

	A = ['7','0','1','2','0','3','0','4','2','3','0','3','2','1','2','0','1','7','0','1']
	B = ['2','3','2','1','5','2','4','5','3','2','5','2']
	seq = input('Please enter "A", "B", or a number sequence (separated by spaces):\n')

	if seq == "A":
		clock(A)
	elif seq == "B":
		clock(B)
	else:
		clock(seq.split())