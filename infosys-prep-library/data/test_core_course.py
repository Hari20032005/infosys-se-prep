"""Unit tests for the Core Course helpers. Run: cd data && python3 test_core_course.py"""
import unittest

import cc_readability as R


class ReadabilityTests(unittest.TestCase):
    def test_strips_code_tables_and_frontmatter(self):
        md = "---\ntitle: x\n---\n# H\n\nShort plain sentence here. Another one follows.\n\n```python\nprint(1)\n```\n\n| a | b |\n|---|---|\n"
        p = R.prose(md)
        self.assertNotIn("print", p)
        self.assertNotIn("title", p)
        self.assertNotIn("|", p)

    def test_counts_and_scores(self):
        r = R.readability("The cat sat on the mat. The dog ran to the park.")
        self.assertEqual(r["sentences"], 2)
        self.assertEqual(r["words"], 12)
        self.assertGreater(r["flesch"], 90)

    def test_hard_prose_scores_lower(self):
        easy = R.readability("It is easy. We can do it now.")["flesch"]
        hard = R.readability("Notwithstanding considerable epistemological complications, the aforementioned methodology necessitates comprehensive reconsideration.")["flesch"]
        self.assertLess(hard, easy)

    def test_list_items_count_as_sentences(self):
        r = R.readability("Steps:\n\n1. Read the question\n2. Find the rule\n3. Check it\n")
        self.assertGreaterEqual(r["sentences"], 3)


if __name__ == "__main__":
    unittest.main()
