with open ('Task 1 All Outputs.txt', 'r') as f:
    eval_code = f.read()
    
files = eval_code.split('File')

memory = files[0]
avg_wer = 0.0
avg_steps_taken = 0
avg_decode_time = 0.0
avg_backtrace_time = 0.0

balance = 0

files = files[1:]

for file in files:
    file = file.split('\n')
    file = list(filter(None, file))
    wer = float(file[2].split(' ')[-2][:-1])
    steps_taken = int(file[5].split(' ')[-2][:-1])
    decode_time = float(file[6].split(' ')[-2][:-1])
    backtrace_time = float(file[7].split(' ')[-2][:-1])

    len_expected = len(file[3].split(' ')) - 1
    len_actual = len(file[4].split(' '))
    
    avg_wer += wer
    avg_steps_taken += steps_taken
    avg_decode_time += decode_time
    avg_backtrace_time += backtrace_time

    balance += len_actual - len_expected

avg_wer /= len(files)
avg_steps_taken /= len(files)
avg_decode_time /= len(files)
avg_backtrace_time /= len(files)
avg_balance = balance / len(files)

print('Memory:', memory)
print('Average WER:', avg_wer)
print('Average Steps Taken:', avg_steps_taken)
print('Average Decode Time:', avg_decode_time)
print('Average Backtrace Time:', avg_backtrace_time)
print('Balance:', balance)
print('Average Balance:', avg_balance)