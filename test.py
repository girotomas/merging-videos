import unittest
from .index import merge_videos
import os

def current_directory():
	return os.path.dirname(os.path.realpath(__file__))

def remove_output_file(filepath):
	try:
	    os.remove(filepath)
	except OSError:
	    pass

outputPath = current_directory() + '/output.mp4'

class TestPackage(unittest.TestCase):

    def test_merge(self):
        remove_output_file(outputPath)
        self.assertTrue(merge_videos([ current_directory() + '/test_video_dont_delete.mp4', current_directory() + '/test_video_dont_delete2.mp4'], outputPath))

if __name__ == '__main__':
    unittest.main()