import os

def is_melt_installed():
	import distutils.spawn
	return distutils.spawn.find_executable("melt")

def install_melt():
		bashCommand = "apt-get update; apt-get install_melt"
		import subprocess
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()

def file_already_exists(ouputPath):
	import os.path
	return os.path.isfile(ouputPath) 

def run_bash_command(bashCommand):
		print('[merging-videos] Running bash command ' + ' '.join(bashCommand))
		import subprocess
		process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
		output, error = process.communicate()
		print('output', output)
		print('error', error)

def merge_videos(filePaths, texts_to_show, outputPath):
	for path in filePaths:
		if not os.path.isabs(path):
			raise Exception(f'[merge-videos] filePaths should all be absolute. {path} is not absolute.')
	if not os.path.isabs(outputPath):
		raise Exception(f'[merge-videos] outputPath should be absolute. {outputPath} is not absolute.')
	try:
		print(f'[merge-videos] joining {" ".join(filePaths)} outputing to {outputPath}.')
		if not is_melt_installed():
			raise Exception('[merge-videos] Error: melt must be installed and an available command install melt with "sudo apt-get update; sudo apt-get install melt"')

		if file_already_exists(outputPath):
			raise Exception(f'[merge-videos] Error: outputPath: {outputPath} file already exists before merging.')
		for filePath, text in zip(filePaths, texts_to_show):
			bashCommand = ['melt', filePath,'-attach',f'dynamictext:{text}', 'bgcolour=0xFFFFFFFF', '-consumer', f'avformat:{filePath + "with_text.mp4"}', 'acodec=libmp3lame', 'vcodec=libx264']
			run_bash_command(bashCommand)
		bashCommand = ["melt"] +  [f + 'with_text.mp4' for f in filePaths] + [ '-consumer', f'avformat:{outputPath}', 'acodec=libmp3lame', 'vcodec=libx264']
		run_bash_command(bashCommand)

		return True
	except Exception as e:
		raise e

