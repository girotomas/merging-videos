import unittest
from index import merge_videos

class TestPackage(unittest.TestCase):

    def test_merge(self):
        self.assertTrue(merge_videos(['./test_video_dont_delete.mp4', './test_video_dont_delete2.mp4'], './output.mp4'))

if __name__ == '__main__':
    unittest.main()