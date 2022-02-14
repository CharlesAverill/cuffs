from tqdm import tqdm

import random
import time

epochs = random.randrange(50, 100)
batch_size = random.choice([16, 32, 64])
training_examples = random.randrange(50, 100)

loss = random.uniform(0.9, 1.0)

for i in range(1, epochs + 1):
	print(f"Epoch {i}/{epochs}")
	bar = tqdm(range(batch_size), bar_format="[{postfix[0]}/{postfix[1]} {bar}] - {postfix[3]}s {postfix[2]}ms/step loss:{postfix[4]} accuracy:{postfix[5]}", postfix=[0]*100)
	begin_time = time.time()
	for j in bar:
		if loss < 0.5:
			loss += random.uniform(-0.02, 0.05)
			if loss <= 0.1:
				loss += 0.1
		else:
			loss += random.uniform(-0.05, 0.02)
		if random.randrange(1, 100) == 55:
			loss -= 0.1
		bar.postfix = [j, 
					   batch_size, 
					   random.randrange(100, 150), 
					   int(round(time.time() - begin_time, 0)), 
					   round(loss, 2),
					   round(1 - loss, 2),]
		bar.refresh()
		time.sleep(bar.postfix[2] / 1000)
