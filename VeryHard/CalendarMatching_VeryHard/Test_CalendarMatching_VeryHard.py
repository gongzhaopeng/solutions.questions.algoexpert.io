import unittest
from SolutionI_CalendarMatching_VeryHard import calendarMatching


class TestCalendarMatching(unittest.TestCase):
    def test_case1(self):
        calendar1 = [
            ["7:00", "7:45"],
            ["8:15", "8:30"],
            ["9:00", "10:30"],
            ["12:00", "14:00"],
            ["14:00", "15:00"],
            ["15:15", "15:30"],
            ["16:30", "18:30"],
            ["20:00", "21:00"]
        ]
        daily_bounds1 = ["6:30", "22:00"]
        calendar2 = [
            ["9:00", "10:00"],
            ["11:15", "11:30"],
            ["11:45", "17:00"],
            ["17:30", "19:00"],
            ["20:00", "22:15"]
        ]
        daily_bounds2 = ["8:00", "22:30"]
        meeting_duration = 30

        expected = [
            ["8:30", "9:00"],
            ["10:30", "11:15"],
            ["19:00", "20:00"]
        ]
        self.assertEqual(expected,
                         calendarMatching(calendar1, daily_bounds1,
                                          calendar2, daily_bounds2,
                                          meeting_duration)
                         )


if __name__ == '__main__':
    unittest.main()
