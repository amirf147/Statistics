# This program allows you to do calculations with small data sets that you copy from somewhere
# For this program it assumes the data values are seperated by a white space

import math


#Replace the data in string with your own data

string = "487 504 501 515 491 496 482 502 508 494 505 501 485 503 507 494 489 501 510 491 503 492 483 501 500 493 505 501 517 500 494 503 500 488 496 500 519 499 495 490 503 500 497 492 510 506 497 499 489 506 502 484 495 498 502 496 512 504 490 497 488 503 512 497 480 509 496 513 499 502 487 499 505 493 498 508 492 498 486 511 499 504 495 500 484 513 509 497 505 510 516 499 495 507 498 514 506 500 508 494"

sample = [int(i) for i in string.split()] # make each number an int in a list


# variables to do with variance and standard deviation

sample_total = sum(sample)

sum_deviation = 0 # holder for the sum of each deviation squared

sample_size = len(sample)

sample_mean = sample_total / sample_size

sample_deviation = [] # holder for deviation from mean for each data point in sample


# derivation of variance and standard deviation

for i in range(sample_size):
    sample_deviation.append(round(sample[i] - sample_mean, 4))

for i in range(sample_size):
    sum_deviation += abs(sample_deviation[i]**2)

sample_variance = sum_deviation / sample_size
    
sample_std = round(math.sqrt(sample_variance), 4)

# standard error of the mean which encompasses 68% of deviations
st_error_mean = round(sample_std / math.sqrt(sample_size), 4)

# maximum likely error in a single measurement
error = round(1.96*(sample_std + st_error_mean), 4)


# z values

sample_z = [] # holds the z value for each data point

for i in range(sample_size):
    sample_z.append(round((sample[i] - sample_mean) / sample_std, 4))


# variables resulting from Sturge's Rule for calculating number of bins

num_bins = round(1 + 3.3*math.log(sample_size, 10), 0) # Sturge's Rule

bin_width = math.ceil((max(sample) - min(sample)) / num_bins)



# variables for Chi-Squared distribution

k_chi = sample_size - 1 # degrees of freedom variable

k_chi_test = sample_size - 2 # k used in the Chi-Squared test



# Chi-Squared goodness of fit test variables

bins = [[],[]] # 2d array for holding measurements in each bin

z_bins = [] # when comparing values to their bins, z values stored here

bin_upper = [] # holds the upper limits of each bin
