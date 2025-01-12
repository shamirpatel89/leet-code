from typing import Dict, List
from unittest import TestCase

class Solution:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     map: Dict[int, List[int]] = {}
    #     result = []

    #     for index, temp in enumerate(temperatures):
    #         result.append(0)
    #         if temp not in map:
    #             map[temp] = [index]
    #         else:
    #             map[temp].append(index)

    #     for index, temp in enumerate(temperatures):
    #         remove_from_map = []
    #         for temp_key, indices in map.items():
    #             if temp > temp_key:
    #                 for temp_index in indices:
    #                     result[temp_index] = index - temp_index
    #                 remove_from_map.append(temp_key)
    #         for i in remove_from_map:
    #             map.pop(i)

    #     return result

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        map: Dict[int, List[int]] = {}
        result = []

        for index, temp in enumerate(temperatures):
            remove_from_map = []
            result.append(0)
            if temp not in map:
                map[temp] = [index]
            else:
                map[temp].append(index)

            for temp_key, indices in map.items():
                if temp > temp_key:
                    for temp_index in indices:
                        result[temp_index] = index - temp_index
                    remove_from_map.append(temp_key)
            for i in remove_from_map:
                map.pop(i)

        return result

class MyTest(TestCase):

    def test_(self):
        solution = Solution()
        cases = [
            {
                'parameter': [73,74,75,71,69,72,76,73],
                'expected': [1,1,4,2,1,1,0,0],
            },
            {
                'parameter': [30,40,50,60],
                'expected': [1,1,1,0],
            },
            {
                'parameter': [30,60,90],
                'expected': [1,1,0],
            },
        ]

        for case in cases:
            with TestCase.subTest(self, **case):
                parameter = case['parameter']
                actual = solution.dailyTemperatures(parameter)
                self.assertEqual(actual, case['expected'])
