from tqdm import tqdm
#This module can be used to display a progress bar in terminal.
for i in tqdm(range(1000000)):
    pass
#This can be populated with other features such as iterable=variable, desc='message', ascii=True, unit='KB', total=total_size
'''Manual control of the tqdm'''
pbar = tqdm(total=100)
for i in range(10):
    sleep(0.1)
    pbar.update(10)
pbar.close()
