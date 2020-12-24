import unittest
from day4 import year_check, height_check, hair_color_pid_check, eye_color_check


class TestYearsValidity(unittest.TestCase):
    def test_byr_valid(self):
        ymin_ymax = (1920, 2002)
        ytest = 2002
        result = year_check(ytest, *ymin_ymax)
        self.assertTrue(
            result, "Birth Year shouldn't be invalid. Years in [1920, 2002] are valid.")

    def test_byr_invalid(self):
        ymin_ymax = (1920, 2002)
        ytest = 2003
        result = year_check(ytest, *ymin_ymax)
        self.assertFalse(
            result, "Birth Year shouldn't be valid. Years before 1920 or after 2002 are invalid.")

    def test_iyr_valid(self):
        ymin_ymax = (2010, 2020)
        ytest = 2014
        result = year_check(ytest, *ymin_ymax)
        self.assertTrue(
            result, "Issue Year shouldn't be invalid. Years in [2010, 2020] are valid.")

    def test_iyr_invalid(self):
        ymin_ymax = (2010, 2020)
        ytest = 2023
        result = year_check(ytest, *ymin_ymax)
        self.assertFalse(
            result, "Issue Year shouldn't be valid. Years before 2010 or after 2020 are invalid.")

    def test_eyr_valid(self):
        ymin_ymax = (2020, 2030)
        ytest = 2025
        result = year_check(ytest, *ymin_ymax)
        self.assertTrue(
            result, "Expiration Year shouldn't be invalid. Years in [2020, 2030] are valid.")

    def test_eyr_invalid(self):
        ymin_ymax = (2020, 2030)
        ytest = 2043
        result = year_check(ytest, *ymin_ymax)
        self.assertFalse(
            result, "Expiration Year shouldn't be valid. Years before 2020 or after 2030 are invalid.")


class TestHeightValidity(unittest.TestCase):
    def test_hgt_in_valid(self):
        hgt = "60in"
        result = height_check(hgt)
        self.assertTrue(
            result, "Height with number AND unit (in) shouldn't be invalid. Values from 59in to 76in are valid.")

    def test_hgt_cm_valid(self):
        hgt = "190cm"
        result = height_check(hgt)
        self.assertTrue(
            result, "Height with number AND unit (cm) shouldn't be invalid. Values from 150cm to 193cm are valid.")

    def test_hgt_in_invalid(self):
        hgt = "190in"
        result = height_check(hgt)
        self.assertFalse(
            result, "Heights smaller than 59in or greater than 76in are invalid.")

    def test_hgt_cm_invalid(self):
        ymin_ymax = (2020, 2030)
        ytest = 2043
        result = year_check(ytest, *ymin_ymax)
        self.assertFalse(
            result, "Heights smaller than 150cm or greater than 193cm are invalid.")


class TestHairColorValidity(unittest.TestCase):
    def test_haircolor_valid(self):
        hcl = "#123abc"
        result = hair_color_pid_check("hcl", hcl)
        self.assertTrue(
            result, "Hair color with leading pound sign (#) AND six characters 0-9 or a-f shouldn't be invalid.")

    def test_haircolor_invalid_char(self):
        hcl = "#123abz"
        result = hair_color_pid_check("hcl", hcl)
        self.assertFalse(
            result, "Hair color with leading pound sign (#) but including g-z within the following six characters should be invalid.")

    def test_haircolor_invalid_format(self):
        hcl = "123abc"
        result = hair_color_pid_check("hcl", hcl)
        self.assertFalse(
            result, "Hair color without leading pound sign (#) should be invalid.")


class TestPIDValidity(unittest.TestCase):
    def test_pid_valid(self):
        pid = "000000001"
        result = hair_color_pid_check("pid", pid)
        self.assertTrue(
            result, "Passport ID is a nine-digit number, including leading zeros.")

    def test_pid_invalid(self):
        pid = "0123456789"
        result = hair_color_pid_check("pid", pid)
        self.assertFalse(
            result, "Passport ID should be a nine-digit number, including leading zeros.")


class TestEyeColorValidity(unittest.TestCase):
    def test_ecl_valid(self):
        ecl = "brn"
        result = eye_color_check(ecl)
        self.assertTrue(
            result, "Eye color should be exactly one of: amb, blu, brn, gry, grn, hzl, oth.")

    def test_ecl_invalid(self):
        ecl = "wat"
        result = eye_color_check(ecl)
        self.assertFalse(
            result, "Eye color should be exactly one of: amb, blu, brn, gry, grn, hzl, oth.")


if __name__ == '__main__':
    unittest.main()
