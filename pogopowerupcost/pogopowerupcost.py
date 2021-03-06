#!/usr/bin/env python
# coding=utf-8

COST_PER_POWERUP = {
	# level: [stardust, candy]
	1.0:  [  200,  1],
	1.5:  [  200,  1],
	2.0:  [  200,  1],
	2.5:  [  200,  1],
	3.0:  [  400,  1],
	3.5:  [  400,  1],
	4.0:  [  400,  1],
	4.5:  [  400,  1],
	5.0:  [  600,  1],
	5.5:  [  600,  1],
	6.0:  [  600,  1],
	6.5:  [  600,  1],
	7.0:  [  800,  1],
	7.5:  [  800,  1],
	8.0:  [  800,  1],
	8.5:  [  800,  1],
	9.0:  [ 1000,  1],
	9.5:  [ 1000,  1],
	10.0: [ 1000,  1],
	10.5: [ 1000,  1],
	11.0: [ 1300,  2],
	11.5: [ 1300,  2],
	12.0: [ 1300,  2],
	12.5: [ 1300,  2],
	13.0: [ 1600,  2],
	13.5: [ 1600,  2],
	14.0: [ 1600,  2],
	14.5: [ 1600,  2],
	15.0: [ 1900,  2],
	15.5: [ 1900,  2],
	16.0: [ 1900,  2],
	16.5: [ 1900,  2],
	17.0: [ 2200,  2],
	17.5: [ 2200,  2],
	18.0: [ 2200,  2],
	18.5: [ 2200,  2],
	19.0: [ 2500,  2],
	19.5: [ 2500,  2],
	20.0: [ 2500,  2],
	20.5: [ 2500,  2],
	21.0: [ 3000,  3],
	21.5: [ 3000,  3],
	22.0: [ 3000,  3],
	22.5: [ 3000,  3],
	23.0: [ 3500,  3],
	23.5: [ 3500,  3],
	24.0: [ 3500,  3],
	24.5: [ 3500,  3],
	25.0: [ 4000,  3],
	25.5: [ 4000,  3],
	26.0: [ 4000,  3],
	26.5: [ 4000,  3],
	27.0: [ 4500,  3],
	27.5: [ 4500,  3],
	28.0: [ 4500,  3],
	28.5: [ 4500,  3],
	29.0: [ 5000,  4],
	29.5: [ 5000,  4],
	30.0: [ 5000,  4],
	30.5: [ 5000,  4],
	31.0: [ 6000,  6],
	31.5: [ 6000,  6],
	32.0: [ 6000,  6],
	32.5: [ 6000,  6],
	33.0: [ 7000,  8],
	33.5: [ 7000,  8],
	34.0: [ 7000,  8],
	34.5: [ 7000,  8],
	35.0: [ 8000, 10],
	35.5: [ 8000, 10],
	36.0: [ 8000, 10],
	36.5: [ 8000, 10],
	37.0: [ 9000, 12],
	37.5: [ 9000, 12],
	38.0: [ 9000, 12],
	38.5: [ 9000, 12],
	39.0: [10000, 15],
	39.5: [10000, 15], # Unconfirmed
	40.0: [10000, 15], # Unconfirmed
	40.5: [10000, 15], # Unconfirmed
}

def calculate_powerup_cost(from_level, to_level):
	total_stardust = 0
	total_candy = 0
	while from_level < to_level:
		cost = COST_PER_POWERUP[from_level]
		stardust, candy = COST_PER_POWERUP[from_level]
		total_stardust += stardust
		total_candy += candy
		from_level += 0.5
	return {
		'stardust': total_stardust,
		'candy': total_candy,
	}
