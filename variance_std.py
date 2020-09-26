import math

string = "487 504 501 515 491 496 482 502 508 494 505 501 485 503 507 494 489 501 510 491 503 492 483 501 500 493 505 501 517 500 494 503 500 488 496 500 519 499 495 490 503 500 497 492 510 506 497 499 489 506 502 484 495 498 502 496 512 504 490 497 488 503 512 497 480 509 496 513 499 502 487 499 505 493 498 508 492 498 486 511 499 504 495 500 484 513 509 497 505 510 516 499 495 507 498 514 506 500 508 494"

numbers = [int(i) for i in string.split()] #make each number an int in a list

numbers_total = 0

sum_deviation = 0
sum_deviation1 = 0

sample_size = len(numbers)

for i in numbers:
    numbers_total += i

numbers_average = numbers_total / 100

numbers_deviation = []

for i in range(sample_size):
    numbers_deviation.append(round(numbers[i] - numbers_average, 4))

for i in range(sample_size):
    sum_deviation += abs(numbers_deviation[i]**2)

numbers_variance = sum_deviation / sample_size
    
numbers_std = round(math.sqrt(numbers_variance), 4)


