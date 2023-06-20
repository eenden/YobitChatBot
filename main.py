import pyautogui
import pyperclip
from time import sleep

def read_phrases():
	with open('phrases.txt', 'r') as f:
		lines = f.readlines()
		return lines

def main():
	lines = read_phrases()
	sleep(10)
	for i, line in enumerate(lines):
		pyautogui.click(1720, 550)
		pyperclip.copy(line)
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.press('enter')
		print(i+1, ' - ', line)
		sleep(30)



if __name__ == '__main__':
	main()