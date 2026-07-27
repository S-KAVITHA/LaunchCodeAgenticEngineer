"""
Unit tests for module_x.py.

Written with unittest (stdlib only, no extra dependencies required); this
suite also runs fine under pytest.
"""

import unittest

from module_x import (
    calculate_discount,
    classify_priority,
    is_valid_project_code,
    normalize_name,
    summarize_order,
)


class NormalizeNameTests(unittest.TestCase):
    def test_title_cases_simple_name(self):
        self.assertEqual(normalize_name("john doe"), "John Doe")

    def test_collapses_internal_whitespace(self):
        self.assertEqual(normalize_name("john   doe"), "John Doe")

    def test_strips_leading_and_trailing_whitespace(self):
        self.assertEqual(normalize_name("  john doe  "), "John Doe")

    def test_handles_tabs_and_newlines(self):
        self.assertEqual(normalize_name("\tjohn\ndoe\t"), "John Doe")

    def test_already_normalized_name_unchanged(self):
        self.assertEqual(normalize_name("Jane Smith"), "Jane Smith")

    def test_non_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            normalize_name(123)

    def test_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            normalize_name(None)

    def test_empty_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            normalize_name("")

    def test_whitespace_only_raises_value_error(self):
        with self.assertRaises(ValueError):
            normalize_name("   \t\n  ")


class CalculateDiscountTests(unittest.TestCase):
    def test_standard_tier_has_no_discount(self):
        self.assertEqual(calculate_discount(100.0, "standard"), 100.0)

    def test_silver_tier_discount(self):
        self.assertEqual(calculate_discount(100.0, "silver"), 95.0)

    def test_gold_tier_discount(self):
        self.assertEqual(calculate_discount(100.0, "gold"), 90.0)

    def test_platinum_tier_discount(self):
        self.assertEqual(calculate_discount(100.0, "platinum"), 85.0)

    def test_tier_is_case_insensitive(self):
        self.assertEqual(calculate_discount(100.0, "GOLD"), 90.0)

    def test_tier_strips_whitespace(self):
        self.assertEqual(calculate_discount(100.0, "  gold  "), 90.0)

    def test_result_is_rounded_to_two_decimals(self):
        self.assertEqual(calculate_discount(10.0 / 3, "silver"), round((10.0 / 3) * 0.95, 2))

    def test_zero_price_returns_zero(self):
        self.assertEqual(calculate_discount(0.0, "platinum"), 0.0)

    def test_negative_price_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_discount(-1.0, "standard")

    def test_unknown_tier_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_discount(100.0, "diamond")

    def test_empty_tier_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_discount(100.0, "")


class ClassifyPriorityTests(unittest.TestCase):
    def test_zero_is_low(self):
        self.assertEqual(classify_priority(0), "low")

    def test_thirty_nine_is_low(self):
        self.assertEqual(classify_priority(39), "low")

    def test_forty_is_medium(self):
        self.assertEqual(classify_priority(40), "medium")

    def test_sixty_nine_is_medium(self):
        self.assertEqual(classify_priority(69), "medium")

    def test_seventy_is_high(self):
        self.assertEqual(classify_priority(70), "high")

    def test_eighty_nine_is_high(self):
        self.assertEqual(classify_priority(89), "high")

    def test_ninety_is_urgent(self):
        self.assertEqual(classify_priority(90), "urgent")

    def test_one_hundred_is_urgent(self):
        self.assertEqual(classify_priority(100), "urgent")

    def test_non_int_raises_type_error(self):
        with self.assertRaises(TypeError):
            classify_priority(50.0)

    def test_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            classify_priority("50")

    def test_negative_score_raises_value_error(self):
        with self.assertRaises(ValueError):
            classify_priority(-1)

    def test_over_hundred_raises_value_error(self):
        with self.assertRaises(ValueError):
            classify_priority(101)


class SummarizeOrderTests(unittest.TestCase):
    def test_empty_list_returns_zeroed_summary(self):
        self.assertEqual(summarize_order([]), {"item_count": 0, "subtotal": 0.0})

    def test_single_item(self):
        result = summarize_order([{"quantity": 2, "unit_price": 5.0}])
        self.assertEqual(result, {"item_count": 2, "subtotal": 10.0})

    def test_multiple_items_are_summed(self):
        items = [
            {"quantity": 2, "unit_price": 5.0},
            {"quantity": 1, "unit_price": 3.5},
        ]
        result = summarize_order(items)
        self.assertEqual(result, {"item_count": 3, "subtotal": 13.5})

    def test_missing_quantity_defaults_to_zero(self):
        result = summarize_order([{"unit_price": 5.0}])
        self.assertEqual(result, {"item_count": 0, "subtotal": 0.0})

    def test_missing_unit_price_defaults_to_zero(self):
        result = summarize_order([{"quantity": 3}])
        self.assertEqual(result, {"item_count": 3, "subtotal": 0.0})

    def test_subtotal_is_rounded_to_two_decimals(self):
        result = summarize_order([{"quantity": 3, "unit_price": 0.1}])
        self.assertEqual(result["subtotal"], 0.3)

    def test_integer_unit_price_is_accepted(self):
        result = summarize_order([{"quantity": 2, "unit_price": 5}])
        self.assertEqual(result, {"item_count": 2, "subtotal": 10.0})

    def test_negative_quantity_raises_value_error(self):
        with self.assertRaises(ValueError):
            summarize_order([{"quantity": -1, "unit_price": 5.0}])

    def test_non_int_quantity_raises_value_error(self):
        with self.assertRaises(ValueError):
            summarize_order([{"quantity": 1.5, "unit_price": 5.0}])

    def test_negative_unit_price_raises_value_error(self):
        with self.assertRaises(ValueError):
            summarize_order([{"quantity": 1, "unit_price": -5.0}])

    def test_non_numeric_unit_price_raises_value_error(self):
        with self.assertRaises(ValueError):
            summarize_order([{"quantity": 1, "unit_price": "5.0"}])


class IsValidProjectCodeTests(unittest.TestCase):
    def test_valid_code_returns_true(self):
        self.assertTrue(is_valid_project_code("AB-1234"))

    def test_lowercase_prefix_returns_false(self):
        self.assertFalse(is_valid_project_code("ab-1234"))

    def test_mixed_case_prefix_returns_false(self):
        self.assertFalse(is_valid_project_code("Ab-1234"))

    def test_wrong_prefix_length_returns_false(self):
        self.assertFalse(is_valid_project_code("ABC-1234"))

    def test_wrong_number_length_returns_false(self):
        self.assertFalse(is_valid_project_code("AB-123"))

    def test_non_digit_number_returns_false(self):
        self.assertFalse(is_valid_project_code("AB-12A4"))

    def test_missing_separator_returns_false(self):
        self.assertFalse(is_valid_project_code("AB1234"))

    def test_too_many_separators_returns_false(self):
        self.assertFalse(is_valid_project_code("AB-12-34"))

    def test_non_string_input_returns_false(self):
        self.assertFalse(is_valid_project_code(1234))

    def test_none_input_returns_false(self):
        self.assertFalse(is_valid_project_code(None))

    def test_empty_string_returns_false(self):
        self.assertFalse(is_valid_project_code(""))


if __name__ == "__main__":
    unittest.main()
