#!/usr/bin/env python
# coding=utf-8

from unittest import TestCase

from pogopowerupcost import calculate_powerup_cost

class TestCalculation(TestCase):

	def test_scenario_1(self):
		cost = calculate_powerup_cost(1, 20)
		self.assertEqual(cost['stardust'], 45000)
		self.assertEqual(cost['candy'], 56)

	def test_scenario_2(self):
		cost = calculate_powerup_cost(4.5, 20)
		self.assertEqual(cost['stardust'], 43000)
		self.assertEqual(cost['candy'], 49)

	def test_scenario_3(self):
		cost = calculate_powerup_cost(36.5, 39)
		self.assertEqual(cost['stardust'], 44000)
		self.assertEqual(cost['candy'], 20)
