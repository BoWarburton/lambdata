#!/usr/bin/env python
"""Tests for lambdata modules."""

from example_module import increment, COLORS
from oop_examples import SocialMediaUser

class ExampleUnitTests(unittest.TestCase):
    """Making sure our examples behave as expected."""
    def test_increment(self):
        """Testing that increment adds one to a number."""
        x1 = 5
        y1 = increment(x1)
        x2 = -106
        y2 = increment(x2)
        # Now we make sure the output is as expected with assertions
        self.assertEqual(y1, 6)
        self.assertEqual(y2, -105)

    def test_increment_random(self):
        x1 = randint(1, 1000000)
        y1 = x1 + 1
        self.assertEqual(y1, x1+ 1)

    def test_colors(self):
        """Presence/absence of expected colors"""
        self.assertIn('Orange', COLORS)
        self.assertNotIn('Aquamarine', COLORS)
        self.assertEqual(len(COLORS), 6)

class SocialMediaUserTests(unittest.TestCase):
    """Test instantiation, use of SocialMediaUser"""
    def test_name(self):
        """Test name assigned correctly"""
        user1 = SocialMediaUser('Jane')
        user2 = SocialMediaUser('Joe')
        self.assertEqual(user1.name, 'Jane')
        self.assertEqual(user2.name, 'Joe')

    def test_default_upvotes(self):
        user1 = SocialMediaUser('Jane')
        self.assertEqual(user1.upvotes, 0)

    def test_unpopular(self):
        user1 = SocialMediaUser('Joe')
        for _ in range(randint(1, 100)):
            user1.receive_upvote()
        self.assertEqual(user1.is_popular(), False)

    def test_popular(self):
        user1 = SocialMediaUser('Jane')
        for _ in range(randint(101, 10000)):
            user1.receive_upvote()
        self.assertEqual(user1.is_popular(), Tru)

if __name__ == '__main__':
    # This conditional is for code that will be run
    # when we execute our file from the command line
    unittest.main()